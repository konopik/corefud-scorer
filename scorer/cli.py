"""Command-line interface for CorefUD scorer and UA scorer."""
import argparse
import sys
from scorer.ua import reader as ua_reader
from scorer.corefud.reader import CorefUDReader
from scorer.conll.reader import CoNLLReader
from scorer.eval import evaluator
from scorer.eval.evaluator import evaluate_non_referrings


def parse_corefud_arguments():
    """Parse command-line arguments for CorefUD scorer."""
    argparser = argparse.ArgumentParser(description="Coreference scorer for documents in CorefUD 1.0 scheme")
    argparser.add_argument('key_file', type=str, help='path to the key/reference file')
    argparser.add_argument('sys_file', type=str, help='path to the system/response file')
    argparser.add_argument('-m', '--metrics', choices=['all', 'lea', 'muc', 'bcub', 'ceafe', 'ceafm', 'blanc', 'mor', 'zero'], nargs='*', default=['all'], help='metrics to be used for evaluation')
    argparser.add_argument('-s', '--keep-singletons', action='store_true', default=False, help='evaluate also singletons; ignored otherwise')
    argparser.add_argument('-a', '--match', type=str, choices=["exact", "partial", "head"], default="head", help='choose the type of mention matching: exact, partial, head')
    argparser.add_argument('-x', '--exact-match', action='store_true', default=False, help='use exact match for matching key and system mentions; overrides the value chosen by --match|-t')
    argparser.add_argument('-z', '--zero-match-method', type=str, choices=["linear", "dependent"], default="dependent", help='if zeros are matched based on their position or based on their dependencies (default: "dependent")')
    args = argparser.parse_args()
    return vars(args)


def corefud_to_ua_args(corefud_args):
    """Convert CorefUD arguments to UA scorer arguments."""
    # arguments to copy with no change
    ua_args = {k:v for k, v in corefud_args.items() if k in ["key_file", "sys_file", "metrics", "keep_singletons", "zero_match_method"]}
    # arguments to be slightly modified
    if corefud_args["exact_match"]:
        ua_args["match"] = "exact"
    elif corefud_args["match"] == "partial":
        ua_args["match"] = "partial-corefud"
    else:
        ua_args["match"] = corefud_args["match"]
    # new arguments
    ua_args["format"] = "corefud"
    ua_args["keep_split_antecedents"] = False
    ua_args["keep_zeros"] = True
    ua_args["evaluate_discourse_deixis"] = False
    ua_args["only_split_antecedent"] = False
    ua_args["allow_boundary_crossing"] = False
    ua_args["np_only"] = False
    ua_args["remove_nested_mentions"] = False
    ua_args["shared_task"] = None
    return ua_args


def main_corefud():
    """Main entry point for corefud_scorer CLI command."""
    try:
        from scorer.ua import scorer_main
        corefud_args = parse_corefud_arguments()
        ua_args = corefud_to_ua_args(corefud_args)
        scorer_main.process_arguments(ua_args)
        scorer_main.evaluate(ua_args)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main_ua():
    """Main entry point for ua_scorer CLI command."""
    try:
        from scorer.ua import scorer_main
        scorer_main.main()
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    # If called directly, default to corefud scorer
    main_corefud()

#!/usr/bin/env python3
"""
CorefUD scorer - Coreference scorer for documents in CorefUD 1.0 scheme.

This script is maintained for backward compatibility.
For new installations, please use the 'corefud_scorer' command directly after installing the package.
"""

from scorer.cli import main_corefud

if __name__ == "__main__":
    main_corefud()

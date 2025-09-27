import matplotlib.pyplot as plt
from pathlib import Path

def save_fig(fig, out_path, dpi=300, tight=True):
    """Save a matplotlib figure to reports/figures with defaults."""
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if tight:
        fig.savefig(out_path, dpi=dpi, bbox_inches='tight')
    else:
        fig.savefig(out_path, dpi=dpi)

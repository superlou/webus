#!/usr/bin/python3
from io import BytesIO

import matplotlib.pyplot as plt


def render_latex(formula, fontsize=12, dpi=300, format_='svg'):
    """Renders LaTeX formula into image.
    """
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, u'${}$'.format(formula), fontsize=fontsize)
    buffer_ = BytesIO()
    fig.savefig(buffer_, dpi=dpi, transparent=True, format=format_, bbox_inches='tight', pad_inches=0.0)
    plt.close(fig)
    return buffer_.getvalue()


if __name__ == '__main__':
    image_bytes = render_latex(
        r'\theta=\theta+C(1+\theta-\beta)\sqrt{1-\theta}succ_mul',
        fontsize=10, dpi=200, format_='png')
    image_bytes = render_latex(
            r'\alpha_{vx}',
            fontsize=10, dpi=200, format_='png')
    with open('formula.png', 'wb') as image_file:
        image_file.write(image_bytes)

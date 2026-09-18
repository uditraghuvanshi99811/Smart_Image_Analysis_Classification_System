import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pathlib import Path

class Evaluator:
    def save_confusion_matrix(self, matrix, classes, output_path):
        fig, ax = plt.subplots(figsize=(6, 5))
        ax.imshow(matrix)
        ax.set_title("Confusion Matrix")
        ax.set_xlabel("Predicted")
        ax.set_ylabel("Actual")
        ax.set_xticks(range(len(classes)), classes, rotation=45, ha="right")
        ax.set_yticks(range(len(classes)), classes)
        for i in range(len(classes)):
            for j in range(len(classes)):
                ax.text(j, i, matrix[i][j], ha="center", va="center")
        fig.tight_layout()
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        fig.savefig(output_path, dpi=150)
        plt.close(fig)

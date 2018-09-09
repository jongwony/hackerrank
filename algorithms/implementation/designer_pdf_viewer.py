def designerPdfViewer(h, word):
    return max(h[ord(c) - ord('A')] for c in word.upper()) * len(word)

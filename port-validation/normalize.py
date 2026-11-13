def normalize_path(path):
    normalized = path.strip().lower()
    return normalized if normalized == "/" else normalized.rstrip("/")

"""Rule-based fallback intent parser for common Git commands."""

def rule_based_intent(text: str, repo_state: str = ""):
    """
    Convert common natural language phrases into Git commands.
    Supports Arabic and English basic commands.
    Returns command string or None if no match.
    """
    text_lower = text.lower().strip()

    # إنشاء مستودع جديد
    if any(word in text_lower for word in [
        "انشاء مستودع", "إنشاء مستودع", "مستودع جديد",
        "init repo", "create repo", "git init"
    ]):
        return "git init"

    # عرض الحالة
    if any(word in text_lower for word in [
        "عرض الحالة", "الحالة", "status", "show status"
    ]):
        return "git status"

    # حفظ التغييرات
    if any(word in text_lower for word in [
        "حفظ التغييرات", "احفظ", "commit", "save changes"
    ]):
        return 'git add . && git commit -m "Update"'

    # عرض السجل
    if any(word in text_lower for word in [
        "السجل", "تاريخ", "log", "history"
    ]):
        return "git log --oneline --graph --decorate --all"

    # إنشاء فرع
    if any(word in text_lower for word in [
        "انشاء فرع", "إنشاء فرع", "فرع جديد", "create branch", "new branch"
    ]):
        return "git branch"

    # استنساخ مستودع
    if any(word in text_lower for word in [
        "استنساخ", "clone", "نسخ مستودع"
    ]):
        return "git clone"

    # رفع التغييرات
    if any(word in text_lower for word in [
        "رفع", "push", "ارفع"
    ]):
        return "git push"

    # سحب التغييرات
    if any(word in text_lower for word in [
        "سحب", "pull", "اسحب"
    ]):
        return "git pull"

    # حذف فرع
    if any(word in text_lower for word in [
        "حذف فرع", "delete branch", "remove branch"
    ]):
        return "git branch -d"

    # دمج فرع
    if any(word in text_lower for word in [
        "دمج فرع", "merge branch", "ادمج"
    ]):
        return "git merge"

    # إضافة ملف
    if any(word in text_lower for word in [
        "إضافة ملف", "اضف ملف", "add file", "stage file"
    ]):
        return "git add"

    # استرجاع تغييرات
    if any(word in text_lower for word in [
        "استرجاع", "تراجع", "undo", "revert"
    ]):
        return "git checkout -- ."

    return None
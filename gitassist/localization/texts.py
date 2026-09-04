"""Text strings for GitAssist (English and Arabic)."""

from gitassist.config import settings

TEXTS = {
    # عام
    "welcome": {"en": "Welcome to GitAssist!", "ar": "مرحبًا بك في GitAssist!"},
    "menu_prompt": {"en": "What would you like to do?", "ar": "ماذا تريد أن تفعل؟"},
    "exit_message": {"en": "Goodbye!", "ar": "وداعًا!"},
    "not_implemented": {"en": "This feature is not implemented yet.", "ar": "هذه الميزة غير منفذة بعد."},
    "help_text": {"en": "Use menu numbers to select actions, 'm' for manual command, 'h' for help, 'q' to quit.", "ar": "استخدم أرقام القائمة للاختيار، 'm' لأمر يدوي، 'h' للمساعدة، 'q' للخروج."},
    "git_installed": {"en": "Git: Installed", "ar": "Git: مثبت"},
    "git_not_installed": {"en": "Git is not installed or not in PATH.", "ar": "Git غير مثبت أو ليس في PATH."},
    "repo_detected": {"en": "Repository: Detected", "ar": "المستودع: موجود"},
    "repo_not_detected": {"en": "Repository: Not detected (not inside a Git repo)", "ar": "المستودع: غير موجود (لست داخل مستودع Git)"},
    "current_branch": {"en": "Current branch: {branch}", "ar": "الفرع الحالي: {branch}"},
    "no_branch": {"en": "Current branch: (no branch)", "ar": "الفرع الحالي: (بدون فرع)"},
    "uncommitted_changes_yes": {"en": "Uncommitted changes: Yes", "ar": "تغييرات غير محفوظة: نعم"},
    "uncommitted_changes_no": {"en": "Uncommitted changes: No", "ar": "تغييرات غير محفوظة: لا"},
    "remote_configured": {"en": "Remote: {remote}", "ar": "المستودع البعيد: {remote}"},
    "remote_not_configured": {"en": "Remote: Not configured", "ar": "المستودع البعيد: غير مضبوط"},
    "ready_message": {"en": "GitAssist is ready. Menu coming in next stage.", "ar": "GitAssist جاهز. القائمة قادمة في المرحلة التالية."},
    "invalid_choice": {"en": "Invalid choice.", "ar": "اختيار غير صالح."},
    "please_enter_number": {"en": "Please enter a number.", "ar": "يرجى إدخال رقم."},
    "input_empty": {"en": "Input cannot be empty.", "ar": "الإدخال لا يمكن أن يكون فارغًا."},

    # القوائم
    "main_menu_title": {"en": "Main Menu", "ar": "القائمة الرئيسية"},
    "create_new_project": {"en": "Create new Git project", "ar": "إنشاء مشروع Git جديد"},
    "open_existing_project": {"en": "Open existing project", "ar": "فتح مشروع موجود"},
    "clone_repository": {"en": "Clone repository", "ar": "استنساخ مستودع"},
    "show_status": {"en": "Show status", "ar": "عرض الحالة"},
    "save_changes": {"en": "Save changes (add/commit)", "ar": "حفظ التغييرات (add/commit)"},
    "view_history": {"en": "View commit history", "ar": "عرض سجل الالتزامات"},
    "manage_branches": {"en": "Manage branches", "ar": "إدارة الفروع"},
    "stash_changes": {"en": "Stash changes", "ar": "حفظ مؤقت (stash)"},
    "manage_files": {"en": "Manage files", "ar": "إدارة الملفات"},
    "synchronize": {"en": "Synchronize with remote", "ar": "مزامنة مع البعيد"},
    "github_info": {"en": "GitHub / Remote Info", "ar": "معلومات GitHub / البعيد"},
    "manual_command": {"en": "Enter a Git command manually", "ar": "إدخال أمر Git يدويًا"},
    "voice_command": {"en": "Voice command", "ar": "أمر صوتي"},
    "exit": {"en": "Exit", "ar": "خروج"},
    "back_to_main": {"en": "Back to main menu", "ar": "العودة إلى القائمة الرئيسية"},

    # سيناريوهات
    "project_name_prompt": {"en": "Project name (repository name):", "ar": "اسم المشروع (اسم المستودع):"},
    "location_prompt": {"en": "Location (leave empty for current directory):", "ar": "الموقع (اتركه فارغًا للمجلد الحالي):"},
    "path_exists_error": {"en": "Path '{path}' already exists.", "ar": "المسار '{path}' موجود بالفعل."},
    "initialize_repo": {"en": "Initializing Git repository...", "ar": "تهيئة مستودع Git..."},
    "repo_initialized": {"en": "Git repository initialized.", "ar": "تم تهيئة مستودع Git."},
    "create_readme_prompt": {"en": "Create README.md?", "ar": "هل تريد إنشاء README.md؟"},
    "add_remote_prompt": {"en": "Add remote repository now?", "ar": "هل تريد إضافة مستودع بعيد الآن؟"},
    "remote_url_prompt": {"en": "Remote URL:", "ar": "رابط المستودع البعيد:"},
    "remote_added": {"en": "Remote 'origin' added.", "ar": "تمت إضافة المستودع البعيد 'origin'."},
    "project_path_prompt": {"en": "Project path:", "ar": "مسار المشروع:"},
    "not_git_repo_error": {"en": "Not a Git repository.", "ar": "ليس مستودع Git."},
    "opened_project": {"en": "Opened: {path}", "ar": "تم الفتح: {path}"},
    "clone_url_prompt": {"en": "Repository URL:", "ar": "رابط المستودع:"},
    "clone_dest_prompt": {"en": "Destination folder (leave empty for default):", "ar": "المجلد الوجهة (اتركه فارغًا للافتراضي):"},
    "clone_completed": {"en": "Clone completed.", "ar": "اكتمل الاستنساخ."},
    "open_cloned_prompt": {"en": "Open cloned repository now?", "ar": "هل تريد فتح المستودع المستنسخ الآن؟"},

    # المزامنة
    "fetch_completed": {"en": "Fetch completed.", "ar": "اكتمل الجلب."},
    "pull_completed": {"en": "Pull completed.", "ar": "اكتمل السحب."},
    "push_completed": {"en": "Push completed.", "ar": "اكتمل الرفع."},
    "check_updates": {"en": "Check remote updates", "ar": "فحص تحديثات البعيد"},
    "behind_remote": {"en": "You are behind the remote branch. Consider pulling changes.", "ar": "أنت متأخر عن الفرع البعيد. يُنصح بسحب التغييرات."},
    "up_to_date": {"en": "Your branch is up to date with remote.", "ar": "فرعك محدث بالنسبة للبعيد."},

    # الفروع
    "branch_management": {"en": "Branch Management", "ar": "إدارة الفروع"},
    "list_branches": {"en": "List branches", "ar": "عرض الفروع"},
    "create_branch": {"en": "Create branch", "ar": "إنشاء فرع"},
    "switch_branch": {"en": "Switch branch", "ar": "التبديل إلى فرع"},
    "delete_branch": {"en": "Delete branch", "ar": "حذف فرع"},
    "merge_branch": {"en": "Merge branch", "ar": "دمج فرع"},
    "new_branch_name": {"en": "New branch name:", "ar": "اسم الفرع الجديد:"},
    "branch_created": {"en": "Branch '{name}' created.", "ar": "تم إنشاء الفرع '{name}'."},
    "branch_to_switch": {"en": "Branch name to switch to:", "ar": "اسم الفرع للتبديل إليه:"},
    "branch_switched": {"en": "Switched to '{name}'.", "ar": "تم التبديل إلى '{name}'."},
    "branch_to_delete": {"en": "Branch name to delete:", "ar": "اسم الفرع للحذف:"},
    "branch_deleted": {"en": "Branch '{name}' deleted.", "ar": "تم حذف الفرع '{name}'."},
    "branch_to_merge": {"en": "Branch name to merge into current:", "ar": "اسم الفرع لدمجه في الحالي:"},
    "confirm_force_delete": {"en": "Force delete (unmerged branches)?", "ar": "حذف قسري (فروع غير مدمجة)؟"},
    "confirm_merge": {"en": "Merge '{name}' into current branch? This may cause conflicts.", "ar": "دمج '{name}' في الفرع الحالي؟ قد يسبب تعارضات."},

    # Stash
    "stash_management": {"en": "Stash Management", "ar": "إدارة الحفظ المؤقت (stash)"},
    "stash_save": {"en": "Save changes (stash)", "ar": "حفظ التغييرات (stash)"},
    "stash_list": {"en": "List stashes", "ar": "عرض المحفوظات"},
    "stash_apply": {"en": "Apply stash", "ar": "تطبيق stash"},
    "stash_pop": {"en": "Pop stash", "ar": "استرجاع stash"},
    "stash_drop": {"en": "Drop stash", "ar": "حذف stash"},
    "stash_message_prompt": {"en": "Stash message (optional):", "ar": "رسالة stash (اختياري):"},
    "changes_stashed": {"en": "Changes stashed.", "ar": "تم حفظ التغييرات."},
    "confirm_drop_stash": {"en": "Drop latest stash?", "ar": "حذف آخر stash؟"},

    # الملفات
    "file_management": {"en": "File Management", "ar": "إدارة الملفات"},
    "create_file": {"en": "Create file", "ar": "إنشاء ملف"},
    "edit_file": {"en": "Edit file (append line)", "ar": "تعديل ملف (إضافة سطر)"},
    "delete_file": {"en": "Delete file", "ar": "حذف ملف"},
    "create_directory": {"en": "Create directory", "ar": "إنشاء مجلد"},
    "filename_prompt": {"en": "File name (e.g., notes.txt):", "ar": "اسم الملف (مثال: notes.txt):"},
    "file_exists_error": {"en": "File '{name}' already exists.", "ar": "الملف '{name}' موجود بالفعل."},
    "file_created": {"en": "File '{name}' created.", "ar": "تم إنشاء الملف '{name}'."},
    "file_to_edit": {"en": "File name to edit:", "ar": "اسم الملف للتعديل:"},
    "file_not_found": {"en": "File '{name}' does not exist.", "ar": "الملف '{name}' غير موجود."},
    "line_to_append": {"en": "Line to append:", "ar": "السطر للإضافة:"},
    "line_appended": {"en": "Line appended to '{name}'.", "ar": "تمت إضافة السطر إلى '{name}'."},
    "file_to_delete": {"en": "File name to delete:", "ar": "اسم الملف للحذف:"},
    "delete_confirm": {"en": "Are you sure you want to delete '{name}'?", "ar": "هل أنت متأكد من حذف '{name}'؟"},
    "file_deleted": {"en": "File '{name}' deleted.", "ar": "تم حذف الملف '{name}'."},
    "dirname_prompt": {"en": "Directory name:", "ar": "اسم المجلد:"},

    # GitHub
    "github_management": {"en": "GitHub / Remote Info", "ar": "معلومات GitHub / البعيد"},
    "show_remote_details": {"en": "Show remote details", "ar": "عرض تفاصيل البعيد"},
    "open_browser": {"en": "Open repository in browser", "ar": "فتح المستودع في المتصفح"},
    "create_github_repo": {"en": "Create GitHub repository", "ar": "إنشاء مستودع GitHub"},
    "github_token_prompt": {"en": "GitHub personal access token:", "ar": "رمز الوصول الشخصي لـ GitHub:"},
    "github_repo_name_prompt": {"en": "Repository name:", "ar": "اسم المستودع:"},
    "github_private_prompt": {"en": "Private repository?", "ar": "مستودع خاص؟"},
    "github_repo_created": {"en": "Repository created: {url}", "ar": "تم إنشاء المستودع: {url}"},
    "github_failed": {"en": "Failed to create repository. Check token and permissions.", "ar": "فشل إنشاء المستودع. تحقق من الرمز والصلاحيات."},

    # الأوامر اليدوية
    "manual_mode_title": {"en": "Manual Command Mode", "ar": "وضع الأوامر اليدوية"},
    "enter_git_command": {"en": "Enter a Git command (e.g., 'git status'):", "ar": "أدخل أمر Git (مثال: 'git status'):"},
    "invalid_command": {"en": "Invalid command. Must start with 'git'.", "ar": "أمر غير صالح. يجب أن يبدأ بـ 'git'."},
    "typo_detected": {"en": "Possible typo detected.", "ar": "احتمال وجود خطأ إملائي."},
    "you_entered": {"en": "You entered: {command}", "ar": "أدخلت: {command}"},
    "did_you_mean": {"en": "Did you mean: {suggestion}", "ar": "هل كنت تقصد: {suggestion}"},
    "execute_corrected": {"en": "Execute corrected command?", "ar": "تنفيذ الأمر المصحح؟"},

    # الذكاء الاصطناعي
    "interpreting": {"en": "Interpreting...", "ar": "جارٍ التفسير..."},
    "ai_suggestion": {"en": "AI suggests: {command}", "ar": "يقترح الذكاء الاصطناعي: {command}"},
    "execute_suggested": {"en": "Execute suggested command?", "ar": "تنفيذ الأمر المقترح؟"},
    "ai_failed": {"en": "AI could not generate a Git command. Try a different phrase or check AI configuration.", "ar": "تعذر على الذكاء الاصطناعي توليد أمر Git. جرب صياغة مختلفة أو تحقق من إعدادات AI."},

    # الصوت
    "voice_unavailable": {"en": "Speech recognition libraries are not installed.", "ar": "مكتبات التعرف على الصوت غير مثبتة."},
    "voice_install_hint": {"en": "Install SpeechRecognition, sounddevice, and numpy to use voice commands.", "ar": "ثبّت SpeechRecognition و sounddevice و numpy لاستخدام الأوامر الصوتية."},
    "voice_listening": {"en": "Listening...", "ar": "جارٍ الاستماع..."},
    "voice_processing": {"en": "Processing speech...", "ar": "جارٍ معالجة الصوت..."},
    "voice_not_understood": {"en": "Could not understand audio.", "ar": "تعذر فهم الصوت."},
    "voice_heard": {"en": "Heard: {text}", "ar": "تم السماع: {text}"},
    "voice_libs_missing": {"en": "SpeechRecognition or sounddevice is missing.", "ar": "مكتبة SpeechRecognition أو sounddevice مفقودة."},

    # Security
    "risk_level": {"en": "Risk level: {level}", "ar": "مستوى الخطورة: {level}"},
    "safer_alternative": {"en": "Safer alternative: {alternative}", "ar": "البديل الأكثر أمانًا: {alternative}"},
    "confirm_continue": {"en": "Do you want to continue? (y/n)", "ar": "هل تريد المتابعة؟ (y/n)"},
    "command_cancelled": {"en": "Command cancelled.", "ar": "تم إلغاء الأمر."},
    "command_failed": {"en": "Command failed: {command}", "ar": "فشل الأمر: {command}"},
    "unexpected_error": {"en": "Unexpected error: {error}", "ar": "خطأ غير متوقع: {error}"},
    "dry_run_message": {"en": "Dry-run mode: would execute: {command}", "ar": "وضع المحاكاة: سيتم تنفيذ: {command}"},

    # Context warnings
    "warning_not_git_repo": {"en": "You are not inside a Git repository.", "ar": "أنت لست داخل مستودع Git."},
    "suggestion_init_or_clone": {"en": "Use 'git init' to create a new repository or 'git clone' to get one.", "ar": "استخدم 'git init' لإنشاء مستودع جديد أو 'git clone' لاستنساخ واحد."},
    "warning_uncommitted_changes": {"en": "You have uncommitted changes that may be overwritten.", "ar": "لديك تغييرات غير محفوظة قد تُستبدل."},
    "suggestion_commit_or_stash": {"en": "Commit or stash your changes first.", "ar": "قم بحفظ التغييرات (commit) أو تخزينها (stash) أولاً."},
    "warning_no_remote": {"en": "No remote repository is configured.", "ar": "لا يوجد مستودع بعيد مكوّن."},
    "suggestion_add_remote": {"en": "Add a remote with 'git remote add origin <url>'.", "ar": "أضف مستودعًا بعيدًا باستخدام 'git remote add origin <url>'."},

    # Error explanations
    "error_not_git_repo": {"en": "You are not inside a Git repository.", "ar": "أنت لست داخل مستودع Git."},
    "error_remote_exists": {"en": "A remote named 'origin' is already configured for this repository.", "ar": "يوجد مستودع بعيد باسم 'origin' مكوّن مسبقًا."},
    "error_push_rejected": {"en": "The remote contains commits that you do not have locally.", "ar": "يحتوي المستودع البعيد على التزامات غير موجودة محليًا."},
    "error_merge_conflict": {"en": "Merge conflict detected in file contents.", "ar": "تم اكتشاف تعارض دمج في محتوى الملفات."},
    "error_local_changes_overwritten": {"en": "You have local modifications that would be lost if you merge or pull.", "ar": "لديك تعديلات محلية ستفقد إذا قمت بالدمج أو السحب."},
    "error_auth_failed": {"en": "Authentication failed or insufficient permissions for the remote repository.", "ar": "فشلت المصادقة أو الصلاحيات غير كافية للمستودع البعيد."},
    "error_not_found": {"en": "The remote repository was not found.", "ar": "لم يتم العثور على المستودع البعيد."},
    "error_unrelated_histories": {"en": "You are trying to merge two branches with unrelated histories.", "ar": "أنت تحاول دمج فرعين لهما تاريخ غير مرتبط."},
    "error_pathspec": {"en": "The specified file or path does not exist in the repository.", "ar": "الملف أو المسار المحدد غير موجود في المستودع."},
    "error_username": {"en": "Git is asking for credentials but no interactive prompt is available.", "ar": "يطلب Git بيانات الاعتماد ولكن لا يوجد موجه تفاعلي متاح."},
}

def get_text(key: str, lang: str = None, **kwargs) -> str:
    if lang is None:
        lang = settings.LANGUAGE
    if key in TEXTS:
        if lang in TEXTS[key]:
            text = TEXTS[key][lang]
        else:
            text = TEXTS[key]["en"]
    else:
        text = key
    if kwargs:
        return text.format(**kwargs)
    return text
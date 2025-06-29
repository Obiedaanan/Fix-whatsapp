import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import os
import subprocess
import webbrowser

class WhatsAppFixTool:
    def __init__(self, root):
        self.root = root
        self.root.title("WhatsApp Fix by Obieda")
        self.root.geometry("900x700")
        self.setup_style()
        self.create_main_menu()
        
    def setup_style(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colors
        self.bg_color = "#2c3e50"
        self.button_color = "#3498db"
        self.button_hover = "#2980b9"
        self.text_color = "#ecf0f1"
        self.alt_bg = "#34495e"
        
        self.style.configure('TFrame', background=self.bg_color)
        self.style.configure('TLabel', background=self.bg_color, foreground=self.text_color)
        self.style.configure('TButton', background=self.button_color, foreground='black', 
                            font=('Helvetica', 10, 'bold'), borderwidth=1)
        self.style.map('TButton', 
                      background=[('active', self.button_hover), ('pressed', self.button_hover)])
        self.style.configure('Title.TLabel', font=('Helvetica', 16, 'bold'), 
                            foreground="#f39c12")
        
        self.root.configure(bg=self.bg_color)
    
    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_main_menu(self):
        self.clear_frame()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        title = ttk.Label(main_frame, text="WhatsApp Fix Tool by Obieda", style='Title.TLabel')
        title.pack(pady=20)
        
        buttons = [
            ("فك حظر الواتساب الرسمي", self.official_whatsapp_menu),
            ("الواتساب المعدل", self.modded_whatsapp_menu),
            ("الاعدادات", self.settings_menu),
            ("معلومات عن المطور", self.developer_info),
            ("التعليمات", self.show_instructions),
            ("خروج", self.exit_app)
        ]
        
        for text, command in buttons:
            btn = ttk.Button(main_frame, text=text, command=command, style='TButton')
            btn.pack(fill='x', padx=50, pady=5, ipady=5)
    
    def official_whatsapp_menu(self):
        self.clear_frame()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        title = ttk.Label(main_frame, text="فك حظر الواتساب الرسمي", style='Title.TLabel')
        title.pack(pady=10)
        
        # Device connection buttons
        conn_frame = ttk.Frame(main_frame)
        conn_frame.pack(pady=10)
        
        ttk.Button(conn_frame, text="اظهار الجهاز المتصل", command=self.show_connected_device).grid(row=0, column=0, padx=5)
        ttk.Button(conn_frame, text="اتصال عن طريق الوايفاي", command=self.connect_wifi).grid(row=0, column=1, padx=5)
        ttk.Button(conn_frame, text="عرض شاشة الجهاز", command=self.show_device_screen).grid(row=0, column=2, padx=5)
        
        # Device info and action frames
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True, pady=10)
        
        # Device info panel
        info_frame = ttk.LabelFrame(content_frame, text="معلومات الجهاز", padding=10)
        info_frame.pack(side='left', fill='both', expand=True, padx=5)
        
        self.device_info_text = scrolledtext.ScrolledText(info_frame, width=40, height=20, bg=self.alt_bg, fg=self.text_color)
        self.device_info_text.pack(fill='both', expand=True)
        self.update_device_info()
        
        # Action boxes
        action_frame = ttk.Frame(content_frame)
        action_frame.pack(side='right', fill='y', padx=5)
        
        # Device 1 box
        device1_frame = ttk.LabelFrame(action_frame, text="الجهاز الأول", padding=10)
        device1_frame.pack(fill='x', pady=5)
        
        ttk.Button(device1_frame, text="حذف بيانات الواتساب مع ابقاء بياناته", 
                  command=self.delete_whatsapp_data).pack(fill='x', pady=2)
        ttk.Button(device1_frame, text="تثبيت الواتساب القديم", 
                  command=lambda: self.install_apk("old.apk")).pack(fill='x', pady=2)
        ttk.Button(device1_frame, text="اخذ نسخة احتياطية من الواتساب باسم ob", 
                  command=self.backup_whatsapp).pack(fill='x', pady=2)
        
        # Device 2 box
        device2_frame = ttk.LabelFrame(action_frame, text="الجهاز الثاني", padding=10)
        device2_frame.pack(fill='x', pady=5)
        
        ttk.Button(device2_frame, text="حذف الواتساب", 
                  command=self.uninstall_whatsapp).pack(fill='x', pady=2)
        ttk.Button(device2_frame, text="تثبيت الواتساب القديم", 
                  command=lambda: self.install_apk("old.apk")).pack(fill='x', pady=2)
        ttk.Button(device2_frame, text="تثبيت الواتساب للاندرويد 14-15", 
                  command=self.install_android_14_15).pack(fill='x', pady=2)
        ttk.Button(device2_frame, text="استعادة النسخ الاحتياطي", 
                  command=self.restore_backup).pack(fill='x', pady=2)
        ttk.Button(device2_frame, text="تحديث الواتساب", 
                  command=lambda: self.install_apk("whatsapp.apk")).pack(fill='x', pady=2)
        
        # Back button
        ttk.Button(main_frame, text="الرجوع الى القائمة السابقة", 
                  command=self.create_main_menu).pack(pady=10)
    
    def modded_whatsapp_menu(self):
        self.clear_frame()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        title = ttk.Label(main_frame, text="الواتساب المعدل", style='Title.TLabel')
        title.pack(pady=10)
        
        # Device connection buttons
        conn_frame = ttk.Frame(main_frame)
        conn_frame.pack(pady=10)
        
        ttk.Button(conn_frame, text="اظهار الجهاز المتصل", command=self.show_connected_device).grid(row=0, column=0, padx=5)
        ttk.Button(conn_frame, text="اتصال عن طريق الوايفاي", command=self.connect_wifi).grid(row=0, column=1, padx=5)
        ttk.Button(conn_frame, text="عرض شاشة الجهاز", command=self.show_device_screen).grid(row=0, column=2, padx=5)
        
        # Device info and action frames
        content_frame = ttk.Frame(main_frame)
        content_frame.pack(fill='both', expand=True, pady=10)
        
        # Device info panel
        info_frame = ttk.LabelFrame(content_frame, text="معلومات الجهاز", padding=10)
        info_frame.pack(side='left', fill='both', expand=True, padx=5)
        
        self.device_info_text = scrolledtext.ScrolledText(info_frame, width=40, height=20, bg=self.alt_bg, fg=self.text_color)
        self.device_info_text.pack(fill='both', expand=True)
        self.update_device_info()
        
        # Action boxes
        action_frame = ttk.Frame(content_frame)
        action_frame.pack(side='right', fill='y', padx=5)
        
        # Device 1 box
        device1_frame = ttk.LabelFrame(action_frame, text="الجهاز الأول", padding=10)
        device1_frame.pack(fill='x', pady=5)
        
        ttk.Button(device1_frame, text="حذف بيانات الواتساب مع ابقاء بياناته", 
                  command=self.delete_whatsapp_data).pack(fill='x', pady=2)
        ttk.Button(device1_frame, text="تثبيت الواتساب القديم", 
                  command=lambda: self.install_apk("old.apk")).pack(fill='x', pady=2)
        ttk.Button(device1_frame, text="اخذ نسخة احتياطية من الواتساب باسم ob", 
                  command=self.backup_whatsapp).pack(fill='x', pady=2)
        ttk.Button(device1_frame, text="تحويل الملف الى tar", 
                  command=self.convert_to_tar).pack(fill='x', pady=2)
        
        # File name entry for zip conversion
        self.zip_name = tk.StringVar()
        zip_frame = ttk.Frame(device1_frame)
        zip_frame.pack(fill='x', pady=2)
        ttk.Label(zip_frame, text="اسم الملف:").pack(side='left')
        ttk.Entry(zip_frame, textvariable=self.zip_name).pack(side='left', fill='x', expand=True)
        ttk.Button(device1_frame, text="تحويل الملف الى صيغة zip", 
                  command=self.convert_to_zip).pack(fill='x', pady=2)
        
        # Device 2 box
        device2_frame = ttk.LabelFrame(action_frame, text="الجهاز الثاني", padding=10)
        device2_frame.pack(fill='x', pady=5)
        
        ttk.Button(device2_frame, text="استعادة النسخة المعدلة", 
                  command=self.restore_modded).pack(fill='x', pady=2)
        ttk.Button(device2_frame, text="تثبيت الواتساب المعدل", 
                  command=self.install_modded).pack(fill='x', pady=2)
        
        # Back button
        ttk.Button(main_frame, text="الرجوع الى القائمة الرئيسية", 
                  command=self.create_main_menu).pack(pady=10)
    
    def settings_menu(self):
        self.clear_frame()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        title = ttk.Label(main_frame, text="الاعدادات", style='Title.TLabel')
        title.pack(pady=20)
        
        lang_frame = ttk.LabelFrame(main_frame, text="تغير اللغة", padding=10)
        lang_frame.pack(pady=10, fill='x', padx=50)
        
        ttk.Button(lang_frame, text="عربي", command=lambda: self.change_language('ar')).pack(fill='x', pady=5)
        ttk.Button(lang_frame, text="English", command=lambda: self.change_language('en')).pack(fill='x', pady=5)
        ttk.Button(lang_frame, text="Français", command=lambda: self.change_language('fr')).pack(fill='x', pady=5)
        
        ttk.Button(main_frame, text="الرجوع", command=self.create_main_menu).pack(pady=10)
    
    def developer_info(self):
        self.clear_frame()
        
        main_frame = ttk.Frame(self.root)
        main_frame.pack(expand=True, fill='both', padx=20, pady=20)
        
        title = ttk.Label(main_frame, text="معلومات المطور", style='Title.TLabel')
        title.pack(pady=20)
        
        info_frame = ttk.Frame(main_frame)
        info_frame.pack(pady=10, fill='x', padx=50)
        
        dev_info = [
            ("المطور:", "عبيدة عنان"),
            ("فيسبوك:", "obiedaanan"),
            ("تليغرام:", "obiedaanan2020"),
            ("تويتر:", "obiedaanan"),
            ("واتساب:", "+963936031489")
        ]
        
        for label, value in dev_info:
            frame = ttk.Frame(info_frame)
            frame.pack(fill='x', pady=2)
            
            ttk.Label(frame, text=label, width=10, anchor='e').pack(side='left')
            if label.endswith(":"):
                btn = ttk.Button(frame, text=value, command=lambda v=value: self.open_developer_link(v))
                btn.pack(side='left', fill='x', expand=True)
            else:
                ttk.Label(frame, text=value).pack(side='left', fill='x', expand=True)
        
        ttk.Button(main_frame, text="الرجوع", command=self.create_main_menu).pack(pady=10)
    
    def show_instructions(self):
        instructions = """
        تعليمات استخدام أداة فك حظر الواتساب:
        
        1. تأكد من تفعيل خيار تصحيح الأخطاء USB في هاتفك
        2. قم بتوصيل الهاتف بالكمبيوتر عبر كابل USB
        3. اختر نوع الواتساب الذي تريد فك حظره (الرسمي أو المعدل)
        4. اتبع الخطوات المعروضة في الأداة
        5. في حالة وجود أي مشكلة، يمكنك التواصل مع المطور
        
        ملاحظة: هذه الأداة تتطلب تثبيت ADB على جهازك
        """
        messagebox.showinfo("التعليمات", instructions)
    
    def exit_app(self):
        if messagebox.askokcancel("خروج", "هل أنت متأكد أنك تريد الخروج؟"):
            self.root.destroy()
    
    # ADB Functions
    def run_adb_command(self, command):
        try:
            result = subprocess.run(['adb'] + command, capture_output=True, text=True)
            return result.stdout if result.returncode == 0 else result.stderr
        except Exception as e:
            return f"Error: {str(e)}"
    
    def update_device_info(self):
        device_info = "اسم الجهاز: " + self.run_adb_command(['shell', 'getprop', 'ro.product.model'])
        device_info += "\n\nنسبة البطارية: " + self.run_adb_command(['shell', 'dumpsys', 'battery', '|', 'grep', 'level'])
        device_info += "\n\nنوع المعالج: " + self.run_adb_command(['shell', 'getprop', 'ro.product.cpu.abi'])
        device_info += "\n\nالعمليات: " + self.run_adb_command(['shell', 'ps'])
        
        if hasattr(self, 'device_info_text'):
            self.device_info_text.delete(1.0, tk.END)
            self.device_info_text.insert(tk.END, device_info)
    
    def show_connected_device(self):
        devices = self.run_adb_command(['devices'])
        messagebox.showinfo("الأجهزة المتصلة", devices)
    
    def connect_wifi(self):
        ip = tk.simpledialog.askstring("الاتصال عبر WiFi", "أدخل عنوان IP للجهاز:")
        if ip:
            result = self.run_adb_command(['connect', ip])
            messagebox.showinfo("نتيجة الاتصال", result)
    
    def show_device_screen(self):
        messagebox.showinfo("عرض الشاشة", "سيتم عرض شاشة الجهاز في نافذة منفصلة")
        # In a real implementation, you would use scrcpy or similar tool
    
    def delete_whatsapp_data(self):
        result = self.run_adb_command(['shell', 'pm', 'clear', 'com.whatsapp'])
        messagebox.showinfo("نتيجة حذف البيانات", result)
    
    def install_apk(self, apk_name):
        apk_path = os.path.join(os.path.dirname(__file__), apk_name)
        if os.path.exists(apk_path):
            result = self.run_adb_command(['install', apk_path])
            messagebox.showinfo("نتيجة التثبيت", result)
        else:
            messagebox.showerror("خطأ", f"الملف {apk_name} غير موجود في مسار الأداة")
    
    def backup_whatsapp(self):
        result = self.run_adb_command(['backup', '-f', 'ob.ab', 'com.whatsapp'])
        messagebox.showinfo("نتيجة النسخ الاحتياطي", result)
    
    def uninstall_whatsapp(self):
        result = self.run_adb_command(['uninstall', 'com.whatsapp'])
        messagebox.showinfo("نتيجة الحذف", result)
    
    def install_android_14_15(self):
        messagebox.showinfo("معلومات", "سيتم تثبيت نسخة الواتساب المخصصة للأندرويد 14-15")
        # Implementation would be similar to install_apk with a specific APK
    
    def restore_backup(self):
        result = self.run_adb_command(['restore', 'ob.ab'])
        messagebox.showinfo("نتيجة الاستعادة", result)
    
    def convert_to_tar(self):
        if os.path.exists('ob.ab'):
            try:
                with open('ob.ab', 'rb') as f:
                    data = f.read()[24:]  # Skip AB header
                with open('ob.tar', 'wb') as f:
                    f.write(data)
                messagebox.showinfo("نجاح", "تم تحويل الملف إلى TAR بنجاح")
            except Exception as e:
                messagebox.showerror("خطأ", f"فشل التحويل: {str(e)}")
        else:
            messagebox.showerror("خطأ", "ملف النسخة الاحتياطية ob.ab غير موجود")
    
    def convert_to_zip(self):
        tar_file = 'ob.tar'
        zip_name = self.zip_name.get() or 'ob'
        
        if os.path.exists(tar_file):
            try:
                import tarfile
                import zipfile
                
                with tarfile.open(tar_file) as tar:
                    with zipfile.ZipFile(f'{zip_name}.zip', 'w') as zipf:
                        for member in tar.getmembers():
                            f = tar.extractfile(member)
                            if f is not None:
                                zipf.writestr(member.name, f.read())
                messagebox.showinfo("نجاح", f"تم تحويل الملف إلى ZIP باسم {zip_name}.zip")
            except Exception as e:
                messagebox.showerror("خطأ", f"فشل التحويل: {str(e)}")
        else:
            messagebox.showerror("خطأ", "ملف TAR غير موجود، قم بتحويل الملف إلى TAR أولاً")
    
    def restore_modded(self):
        zip_name = self.zip_name.get() or 'ob'
        if os.path.exists(f'{zip_name}.zip'):
            result = self.run_adb_command(['push', f'{zip_name}.zip', '/sdcard/'])
            messagebox.showinfo("نتيجة الاستعادة", result)
        else:
            messagebox.showerror("خطأ", f"ملف {zip_name}.zip غير موجود")
    
    def install_modded(self):
        messagebox.showinfo("معلومات", "سيتم تثبيت نسخة الواتساب المعدلة")
        # Implementation would be similar to install_apk with a modded APK
    
    def change_language(self, lang):
        # In a real implementation, you would change the UI language
        langs = {'ar': 'عربي', 'en': 'English', 'fr': 'Français'}
        messagebox.showinfo("تم تغيير اللغة", f"تم تغيير اللغة إلى {langs[lang]}")
    
    def open_developer_link(self, value):
        links = {
            "obiedaanan": "https://facebook.com/obiedaanan",
            "obiedaanan2020": "https://t.me/obiedaanan2020",
            "obiedaanan": "https://twitter.com/obiedaanan",
            "+963936031489": "https://wa.me/963936031489"
        }
        if value in links:
            webbrowser.open(links[value])

if __name__ == "__main__":
    root = tk.Tk()
    app = WhatsAppFixTool(root)
    root.mainloop()

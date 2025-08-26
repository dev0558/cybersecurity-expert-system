import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

class CybersecurityExpertSystem:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_ui()
        self.history = []
        
        # knowledge base
        self.tools_db = {
            'nessus': {
                'name': 'Nessus', 'description': 'Industry-standard vulnerability scanner',
                'type': 'vulnerability', 'gui': True, 'os': ['windows', 'linux', 'macos'],
                'level': ['beginner', 'intermediate', 'advanced'], 'score': 0.9
            },
            'wireshark': {
                'name': 'Wireshark', 'description': 'Network protocol analyzer and packet capture',
                'type': 'network_monitoring', 'gui': True, 'os': ['windows', 'linux', 'macos'],
                'level': ['beginner', 'intermediate', 'advanced'], 'score': 0.95
            },
            'metasploit': {
                'name': 'Metasploit', 'description': 'Penetration testing framework',
                'type': 'penetration_testing', 'gui': True, 'os': ['linux', 'windows'],
                'level': ['intermediate', 'advanced'], 'score': 0.9
            },
            'kali_linux': {
                'name': 'Kali Linux', 'description': 'Penetration testing Linux distribution',
                'type': 'penetration_testing', 'gui': True, 'os': ['linux'],
                'level': ['intermediate', 'advanced'], 'score': 0.95
            },
            'snort': {
                'name': 'Snort', 'description': 'Network intrusion detection system',
                'type': 'intrusion_detection', 'gui': False, 'os': ['linux', 'windows'],
                'level': ['advanced'], 'score': 0.85
            },
            'splunk': {
                'name': 'Splunk', 'description': 'Security information and event management',
                'type': 'siem', 'gui': True, 'os': ['windows', 'linux', 'macos'],
                'level': ['intermediate', 'advanced'], 'score': 0.92
            },
            'burp_suite': {
                'name': 'Burp Suite', 'description': 'Web application security testing',
                'type': 'web_security', 'gui': True, 'os': ['windows', 'linux', 'macos'],
                'level': ['intermediate', 'advanced'], 'score': 0.9
            },
            'nmap': {
                'name': 'Nmap', 'description': 'Network discovery and security auditing',
                'type': 'network_scanning', 'gui': False, 'os': ['linux', 'windows', 'macos'],
                'level': ['intermediate', 'advanced'], 'score': 0.88
            },
            'openvas': {
                'name': 'OpenVAS', 'description': 'Open-source vulnerability assessment',
                'type': 'vulnerability', 'gui': True, 'os': ['linux'],
                'level': ['intermediate', 'advanced'], 'score': 0.82
            },
            'suricata': {
                'name': 'Suricata', 'description': 'High-performance network IDS/IPS',
                'type': 'intrusion_detection', 'gui': False, 'os': ['linux'],
                'level': ['advanced'], 'score': 0.87
            }
        }
    
    def setup_ui(self):
        self.root.title("🔐 Cybersecurity Controls Expert")
        self.root.geometry("1200x800")
        self.root.configure(bg='#1a1a2e')
        
        main_frame = tk.Frame(self.root, bg='#1a1a2e')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.create_header(main_frame)
        
        content_frame = tk.Frame(main_frame, bg='#1a1a2e')
        content_frame.pack(fill='both', expand=True, pady=20)
        
        self.create_input_panel(content_frame)
        self.create_results_panel(content_frame)
    
    def create_header(self, parent):
        header_frame = tk.Frame(parent, bg='#16213e', relief='flat', bd=2)
        header_frame.pack(fill='x', pady=(0, 20))
        
        title_label = tk.Label(header_frame, text="🔐 Cybersecurity Controls Expert",
                              font=('Arial', 28, 'bold'), bg='#16213e', fg='#00d4ff')
        title_label.pack(pady=10)
        
        subtitle_label = tk.Label(header_frame, text="Find the perfect security tools for your needs",
                                 font=('Arial', 14, 'bold'), bg='#16213e', fg='#a0a0a0')
        subtitle_label.pack(pady=(0, 10))
    
    def create_input_panel(self, parent):
        left_frame = tk.Frame(parent, bg='#16213e', relief='flat', bd=2)
        left_frame.pack(side='left', fill='y', padx=(0, 10))
        
        form_title = tk.Label(left_frame, text="📋 Your Requirements",
                             font=('Arial', 16, 'bold'), bg='#16213e', fg='#00d4ff')
        form_title.pack(pady=(15, 20))
        
        # Create dropdowns
        self.create_dropdown(left_frame, "💻 Operating System", 
                           ['Windows', 'Linux', 'MacOS', 'Any'], 'os_var')
        self.create_dropdown(left_frame, "🎯 Security Goal",
                           ['Vulnerability Assessment', 'Network Monitoring', 'Penetration Testing', 
                            'Web Security Testing', 'Intrusion Detection', 'SIEM/Log Analysis', 
                            'Network Scanning', 'General Security'], 'goal_var')
        self.create_dropdown(left_frame, "🎓 Experience Level",
                           ['Beginner', 'Intermediate', 'Advanced'], 'level_var')
        self.create_dropdown(left_frame, "💰 Budget Range",
                           ['Free/Open Source', 'Low Cost', 'Medium Cost', 'Enterprise', 'Any'], 'budget_var')
        self.create_dropdown(left_frame, "🖥️ Interface",
                           ['GUI Preferred', 'Command Line OK', 'No Preference'], 'interface_var')
        
        self.create_buttons(left_frame)
    
    def create_dropdown(self, parent, label_text, values, var_name):
        dropdown_frame = tk.Frame(parent, bg='#16213e')
        dropdown_frame.pack(fill='x', padx=15, pady=8)
        
        label = tk.Label(dropdown_frame, text=label_text, font=('Arial', 10, 'bold'),
                        bg='#16213e', fg='#ffffff')
        label.pack(anchor='w', pady=(0, 3))
        
        var = tk.StringVar()
        setattr(self, var_name, var)
        
        style = ttk.Style()
        style.configure('Custom.TCombobox', fieldbackground='#2a2d3a',
                       background='#2a2d3a', foreground='#ffffff')
        
        combo = ttk.Combobox(dropdown_frame, textvariable=var, values=values,
                            state="readonly", font=('Arial', 9), style='Custom.TCombobox')
        combo.pack(fill='x')
        
        return combo
    
    def create_buttons(self, parent):
        button_frame = tk.Frame(parent, bg='#16213e')
        button_frame.pack(fill='x', padx=15, pady=20)
        
        recommend_btn = tk.Button(button_frame, text="Get Recommendations",
                                 command=self.get_recommendations, font=('Arial', 12, 'bold'),
                                 bg='#00d4ff', fg='#000000', relief='flat',
                                 padx=15, pady=8, cursor='hand2')
        recommend_btn.pack(fill='x', pady=(0, 8))
        
        clear_btn = tk.Button(button_frame, text="🗑️ Clear All",
                             command=self.clear_form, font=('Arial', 10),
                             bg='#00d4ff', fg='#000000', relief='flat',
                             padx=12, pady=6, cursor='hand2')
        clear_btn.pack(fill='x', pady=(0, 8))
        
        history_btn = tk.Button(button_frame, text="📊 History",
                               command=self.show_history, font=('Arial', 10),
                               bg='#00d4ff', fg='#000000', relief='flat',
                               padx=12, pady=6, cursor='hand2')
        history_btn.pack(fill='x')
    
    def create_results_panel(self, parent):
        right_frame = tk.Frame(parent, bg='#16213e', relief='flat', bd=2)
        right_frame.pack(side='right', fill='both', expand=True, padx=(10, 0))
        
        results_title = tk.Label(right_frame, text="💡 Recommendations",
                                font=('Arial', 16, 'bold'), bg='#16213e', fg='#00d4ff')
        results_title.pack(pady=(15, 15))
        
        text_frame = tk.Frame(right_frame, bg='#16213e')
        text_frame.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        self.results_text = tk.Text(text_frame, wrap='word', font=('Arial', 20),
                                   bg='#2a2d3a', fg='#ffffff', relief='flat',
                                   padx=12, pady=12, insertbackground='#00d4ff')
        
        scrollbar = tk.Scrollbar(text_frame, orient='vertical', command=self.results_text.yview)
        self.results_text.configure(yscrollcommand=scrollbar.set)
        
        self.results_text.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        self.show_welcome()
    
    def show_welcome(self):
        welcome_msg = """🔐 Welcome to Cybersecurity Tool Advisor!

This expert system helps you find the right cybersecurity tools based on 
your specific needs and requirements.

How to use:
1. Fill out your requirements in the left panel
2. Click "Get Recommendations" to see personalized suggestions
3. Review the recommended tools with confidence scores
4. Use the history feature to track your searches

What we consider:
• Your operating system compatibility
• Security goals and objectives
• Experience level and technical skills
• Budget constraints
• Interface preferences

Ready to get started? Fill out the form and click "Get Recommendations"!



"""
        self.results_text.insert('end', welcome_msg)
        self.results_text.config(state='disabled')
    
    def get_recommendations(self):
        if not self.validate_inputs():
            messagebox.showwarning("Incomplete Form", "Please fill out the required fields.")
            return
        
        user_inputs = self.collect_inputs()
        recommendations = self.generate_recommendations(user_inputs)
        self.save_to_history(user_inputs, recommendations)
        self.display_results(user_inputs, recommendations)
    
    def validate_inputs(self):
        required_fields = [self.os_var, self.goal_var, self.level_var]
        return all(var.get() for var in required_fields)
    
    def collect_inputs(self):
        return {
            'os': self.os_var.get().lower(),
            'goal': self.goal_var.get(),
            'level': self.level_var.get().lower(),
            'budget': self.budget_var.get(),
            'interface': self.interface_var.get()
        }
    
    def generate_recommendations(self, inputs):
        goal_mapping = {
            'Vulnerability Assessment': 'vulnerability',
            'Network Monitoring': 'network_monitoring',
            'Penetration Testing': 'penetration_testing',
            'Web Security Testing': 'web_security',
            'Intrusion Detection': 'intrusion_detection',
            'SIEM/Log Analysis': 'siem',
            'Network Scanning': 'network_scanning',
            'General Security': 'general'
        }
        
        recommendations = []
        target_type = goal_mapping.get(inputs['goal'], 'general')
        
        for tool_id, tool_data in self.tools_db.items():
            confidence = 0
            reasons = []
            
            # OS compatibility
            if inputs['os'] == 'any' or inputs['os'] in tool_data['os']:
                confidence += 0.3
                reasons.append(f"✓ Compatible with {inputs['os']}")
            else:
                continue
            
            # Goal match
            if target_type == 'general' or tool_data['type'] == target_type:
                confidence += 0.4
                reasons.append(f"✓ Matches your {inputs['goal']} needs")
            
            # Experience level
            if inputs['level'] in tool_data['level']:
                confidence += 0.2
                reasons.append(f"✓ Suitable for {inputs['level']} level")
            
            # Interface preference
            if inputs['interface'] == 'GUI Preferred' and tool_data['gui']:
                confidence += 0.1
                reasons.append("✓ Has graphical interface")
            elif inputs['interface'] == 'Command Line OK' and not tool_data['gui']:
                confidence += 0.1
                reasons.append("✓ Command-line tool")
            
            final_confidence = confidence * tool_data['score']
            
            if final_confidence > 0.3:
                recommendations.append({
                    'tool': tool_data,
                    'confidence': final_confidence,
                    'reasons': reasons
                })
        
        recommendations.sort(key=lambda x: x['confidence'], reverse=True)
        return recommendations[:5]
    
    def display_results(self, inputs, recommendations):
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, 'end')
        
        timestamp = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        header = f"""🔍 Your Cybersecurity Tool Recommendations
Generated: {timestamp}

📊 Your Profile:
• System: {inputs['os'].title()}
• Goal: {inputs['goal']}
• Level: {inputs['level'].title()}
• Budget: {inputs['budget']}
• Interface: {inputs['interface']}



"""
        self.results_text.insert('end', header)
        
        if not recommendations:
            no_results = """❌ No suitable tools found for your criteria.

Try adjusting your requirements:
• Consider expanding your OS compatibility
• Try a different experience level
• Adjust your interface preferences
"""
            self.results_text.insert('end', no_results)
        else:
            for i, rec in enumerate(recommendations, 1):
                tool = rec['tool']
                confidence = rec['confidence'] * 100
                
                if confidence >= 80:
                    badge = "🟢 EXCELLENT"
                elif confidence >= 65:
                    badge = "🟡 GOOD"
                else:
                    badge = "🟠 FAIR"
                
                tool_info = f"""#{i}. {tool['name']} {badge}
Confidence: {confidence:.0f}%

📝 {tool['description']}

Why this tool fits:"""
                
                for reason in rec['reasons']:
                    tool_info += f"\n   {reason}"
                
                tool_info += f"""

💻 Systems: {', '.join([os.title() for os in tool['os']])}
🖥️ Interface: {'GUI Available' if tool['gui'] else 'Command Line Only'}
👥 Best for: {', '.join([level.title() for level in tool['level']])}

{'─' * 70}

"""
                self.results_text.insert('end', tool_info)
            
            footer = f"""🎉 Found {len(recommendations)} great tools for you!

 Tips:
• Higher confidence scores indicate better matches
• Consider trying multiple tools for comprehensive coverage
• Start with "Excellent" matches first

Need different suggestions? Adjust your preferences and search again!
"""
            self.results_text.insert('end', footer)
        
        self.results_text.config(state='disabled')
    
    def save_to_history(self, inputs, recommendations):
        self.history.append({
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'inputs': inputs,
            'results_count': len(recommendations)
        })
    
    def clear_form(self):
        for var in [self.os_var, self.goal_var, self.level_var, self.budget_var, self.interface_var]:
            var.set('')
        
        self.results_text.config(state='normal')
        self.results_text.delete(1.0, 'end')
        self.show_welcome()
    
    def show_history(self):
        if not self.history:
            messagebox.showinfo("History", "No search history available yet.")
            return
        
        history_window = tk.Toplevel(self.root)
        history_window.title("📊 Search History")
        history_window.geometry("600x400")
        history_window.configure(bg='#1a1a2e')
        
        history_frame = tk.Frame(history_window, bg='#16213e')
        history_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        title_label = tk.Label(history_frame, text="📊 Your Search History",
                              font=('Arial', 16, 'bold'), bg='#16213e', fg='#00d4ff')
        title_label.pack(pady=(10, 20))
        
        history_text = tk.Text(history_frame, wrap='word', font=('Arial', 10),
                              bg='#2a2d3a', fg='#ffffff', relief='flat', padx=15, pady=15)
        history_text.pack(fill='both', expand=True)
        
        history_content = f"Total searches: {len(self.history)}\n{'═' * 40}\n\n"
        
        for i, entry in enumerate(reversed(self.history), 1):
            history_content += f"#{i} - {entry['timestamp']}\n"
            history_content += f"   OS: {entry['inputs']['os'].title()}\n"
            history_content += f"   Goal: {entry['inputs']['goal']}\n"
            history_content += f"   Level: {entry['inputs']['level'].title()}\n"
            history_content += f"   Results: {entry['results_count']} tools found\n"
            history_content += "─" * 30 + "\n\n"
        
        history_text.insert('end', history_content)
        history_text.config(state='disabled')
    
    def run(self):
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - 600
        y = (self.root.winfo_screenheight() // 2) - 400
        self.root.geometry(f"+{x}+{y}")
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    app = CybersecurityExpertSystem()
    app.run()

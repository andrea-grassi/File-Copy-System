import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar

class FileCopySystem:
    def __init__(self, root):
        self.root = root
        self.root.title("File Copy System")
        self.root.geometry('500x400')
        
        # Variabile per salvare la scelta dell'utente su "Applica a tutti"
        self.apply_to_all = None
        
        # Label per la cartella sorgente
        self.src_label = tk.Label(root, text="Sorgente:", font=("Arial", 12))
        self.src_label.pack(pady=10)
        
        # Entry per mostrare la cartella sorgente
        self.src_entry = tk.Entry(root, width=50)
        self.src_entry.pack(pady=5)
        
        # Pulsante per selezionare la cartella sorgente
        self.src_button = tk.Button(root, text="Seleziona Cartella Sorgente", command=self.select_source)
        self.src_button.pack(pady=5)
        
        # Label per la cartella destinazione
        self.dst_label = tk.Label(root, text="Destinazione:", font=("Arial", 12))
        self.dst_label.pack(pady=10)
        
        # Entry per mostrare la cartella destinazione
        self.dst_entry = tk.Entry(root, width=50)
        self.dst_entry.pack(pady=5)
        
        # Pulsante per selezionare la cartella destinazione
        self.dst_button = tk.Button(root, text="Seleziona Cartella Destinazione", command=self.select_destination)
        self.dst_button.pack(pady=5)
        
        # Barra di progresso
        self.progress = Progressbar(root, orient=tk.HORIZONTAL, length=400, mode='determinate')
        self.progress.pack(pady=20)
        
        # Pulsante per avviare la copia
        self.copy_button = tk.Button(root, text="Copia e Incolla", command=self.copy_files)
        self.copy_button.pack(pady=10)
        
        # Area di log per visualizzare lo stato della copia
        self.log_text = tk.Text(root, height=80, width=60)
        self.log_text.pack(pady=10)
    
    def select_source(self):
        """Apre un dialogo per selezionare la cartella sorgente"""
        src_folder = filedialog.askdirectory()
        if src_folder:
            self.src_entry.delete(0, tk.END)
            self.src_entry.insert(0, src_folder)
    
    def select_destination(self):
        """Apre un dialogo per selezionare la cartella destinazione"""
        dst_folder = filedialog.askdirectory()
        if dst_folder:
            self.dst_entry.delete(0, tk.END)
            self.dst_entry.insert(0, dst_folder)
    
    def ask_overwrite(self, file_name):
        """Chiede all'utente se sovrascrivere il file esistente, con opzione di applicare a tutti"""
        if self.apply_to_all is not None:
            return self.apply_to_all
        
        # Crea una finestra di dialogo per chiedere conferma
        overwrite_dialog = tk.Toplevel(self.root)
        overwrite_dialog.title("Conferma Sostituzione")
        
        label = tk.Label(overwrite_dialog, text=f"Il file '{file_name}' esiste già. Vuoi sostituirlo?")
        label.pack(pady=10)
        
        apply_to_all_var = tk.IntVar()
        
        # Checkbox per applicare a tutti
        apply_to_all_checkbox = tk.Checkbutton(overwrite_dialog, text="Applica a tutti i file", variable=apply_to_all_var)
        apply_to_all_checkbox.pack(pady=5)
        
        # Funzione per chiudere la finestra con la risposta dell'utente
        def on_yes():
            self.apply_to_all = True if apply_to_all_var.get() == 1 else None
            overwrite_dialog.destroy()
            overwrite_dialog.result = True
        
        def on_no():
            self.apply_to_all = False if apply_to_all_var.get() == 1 else None
            overwrite_dialog.destroy()
            overwrite_dialog.result = False
        
        # Pulsanti per Sì e No
        yes_button = tk.Button(overwrite_dialog, text="Sì", command=on_yes)
        yes_button.pack(side=tk.LEFT, padx=20, pady=10)
        
        no_button = tk.Button(overwrite_dialog, text="No", command=on_no)
        no_button.pack(side=tk.RIGHT, padx=20, pady=10)
        
        # Attendi la risposta dell'utente
        overwrite_dialog.wait_window(overwrite_dialog)
        
        return overwrite_dialog.result
    
    def copy_files(self):
        """Copia i file dalla cartella sorgente a quella destinazione"""
        src = self.src_entry.get()
        dst = self.dst_entry.get()
        
        if not src or not dst:
            messagebox.showwarning("Attenzione", "Seleziona sia una cartella sorgente che una destinazione")
            return
        
        # Resetta l'opzione "Applica a tutti"
        self.apply_to_all = None
        
        # Conta il numero totale di file per la barra di progresso
        total_files = sum([len(files) for r, d, files in os.walk(src)])
        copied_files = 0
        
        # Esegui la copia ricorsiva
        for root_dir, dirs, files in os.walk(src):
            # Ottieni il percorso relativo per mantenere la struttura delle sottocartelle
            relative_path = os.path.relpath(root_dir, src)
            dest_dir = os.path.join(dst, relative_path)
            
            # Crea la cartella destinazione se non esiste
            if not os.path.exists(dest_dir):
                os.makedirs(dest_dir)
            
            # Copia i file nella cartella destinazione
            for file in files:
                src_file = os.path.join(root_dir, file)
                dest_file = os.path.join(dest_dir, file)
                
                # Verifica se il file già esiste e chiedi conferma
                if os.path.exists(dest_file):
                    overwrite = self.ask_overwrite(file)
                    if not overwrite:
                        continue
                
                # Copia il file
                shutil.copy2(src_file, dest_file)
                copied_files += 1
                
                # Aggiorna la barra di progresso e il log
                self.progress['value'] = (copied_files / total_files) * 100
                self.log_text.insert(tk.END, f"Copiato: {src_file} -> {dest_file}\n")
                self.log_text.see(tk.END)
                self.root.update_idletasks()
        
        messagebox.showinfo("Completato", "Copia completata con successo!")

# Avvia l'interfaccia grafica
if __name__ == "__main__":
    root = tk.Tk()
    app = FileCopySystem(root)
    root.mainloop()

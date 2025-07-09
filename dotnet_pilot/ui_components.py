import tkinter as tk
from tkinter import ttk
from .commands import run_command
from .utils import browse_package_file

def create_project_tab(notebook, working_directory, append_output_func):
    frame = ttk.Frame(notebook, padding="10")
    notebook.add(frame, text="Project Management")
    
    # Project creation
    create_frame = ttk.LabelFrame(frame, text="Create New Project", padding="10")
    create_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    create_frame.columnconfigure(1, weight=1)
    
    templates = ['console', 'classlib', 'webapi', 'mvc', 'blazor', 'winforms', 'wpf', 'worker', 'xunit']
    
    ttk.Label(create_frame, text="Template:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
    template_var = tk.StringVar(value='console')
    template_combo = ttk.Combobox(create_frame, textvariable=template_var, values=templates, width=15)
    template_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
    
    ttk.Label(create_frame, text="Name:").grid(row=0, column=2, sticky=tk.W, padx=(10, 5))
    project_name_var = tk.StringVar()
    name_entry = ttk.Entry(create_frame, textvariable=project_name_var, width=20)
    name_entry.grid(row=0, column=3, sticky=tk.W, padx=(0, 10))
    
    create_btn = ttk.Button(create_frame, text="Create Project", 
                           command=lambda: run_command(f"dotnet new {template_var.get()}" +
                                                          (f" -n {project_name_var.get()}" if project_name_var.get() else ""), working_directory, append_output_func))
    create_btn.grid(row=0, column=4, padx=(10, 0))
    
    # Solution management
    sln_frame = ttk.LabelFrame(frame, text="Solution Management", padding="10")
    sln_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    sln_frame.columnconfigure(1, weight=1)
    
    ttk.Button(sln_frame, text="Create Solution", 
              command=lambda: run_command("dotnet new sln", working_directory, append_output_func)).grid(row=0, column=0, padx=(0, 5))
    
    ttk.Label(sln_frame, text="Add Project:").grid(row=0, column=1, sticky=tk.W, padx=(10, 5))
    add_project_var = tk.StringVar()
    add_entry = ttk.Entry(sln_frame, textvariable=add_project_var, width=25)
    add_entry.grid(row=0, column=2, sticky=tk.W, padx=(0, 5))
    
    ttk.Button(sln_frame, text="Add to Solution", 
              command=lambda: run_command(f"dotnet sln add {add_project_var.get()}" if add_project_var.get() else "", working_directory, append_output_func)).grid(row=0, column=3, padx=(5, 0))
    
    # References and packages
    ref_frame = ttk.LabelFrame(frame, text="References & Packages", padding="10")
    ref_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    ref_frame.columnconfigure(1, weight=1)
    
    ttk.Label(ref_frame, text="Package:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
    package_var = tk.StringVar()
    package_entry = ttk.Entry(ref_frame, textvariable=package_var, width=30)
    package_entry.grid(row=0, column=1, sticky=tk.W, padx=(0, 5))
    
    ttk.Button(ref_frame, text="Add Package", 
              command=lambda: run_command(f"dotnet add package {package_var.get()}" if package_var.get() else "", working_directory, append_output_func)).grid(row=0, column=2, padx=(5, 0))
    
    ttk.Label(ref_frame, text="Reference:").grid(row=1, column=0, sticky=tk.W, padx=(0, 5), pady=(5, 0))
    reference_var = tk.StringVar()
    ref_entry = ttk.Entry(ref_frame, textvariable=reference_var, width=30)
    ref_entry.grid(row=1, column=1, sticky=tk.W, padx=(0, 5), pady=(5, 0))
    
    ttk.Button(ref_frame, text="Add Reference", 
              command=lambda: run_command(f"dotnet add reference {reference_var.get()}" if reference_var.get() else "", working_directory, append_output_func)).grid(row=1, column=2, padx=(5, 0), pady=(5, 0))

def create_build_tab(notebook, working_directory, append_output_func):
    frame = ttk.Frame(notebook, padding="10")
    notebook.add(frame, text="Build & Run")
    
    # Build configuration
    config_frame = ttk.LabelFrame(frame, text="Build Configuration", padding="10")
    config_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    
    ttk.Label(config_frame, text="Configuration:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
    build_config_var = tk.StringVar(value='Debug')
    config_combo = ttk.Combobox(config_frame, textvariable=build_config_var, 
                               values=['Debug', 'Release'], width=10, state="readonly")
    config_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
    
    ttk.Label(config_frame, text="Verbosity:").grid(row=0, column=2, sticky=tk.W, padx=(10, 5))
    verbosity_var = tk.StringVar(value='normal')
    verbosity_combo = ttk.Combobox(config_frame, textvariable=verbosity_var,
                                  values=['quiet', 'minimal', 'normal', 'detailed', 'diagnostic'], 
                                  width=10, state="readonly")
    verbosity_combo.grid(row=0, column=3, sticky=tk.W)
    
    # Build operations
    build_frame = ttk.LabelFrame(frame, text="Build Operations", padding="10")
    build_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    
    # Build with configuration
    ttk.Button(build_frame, text="Build", 
              command=lambda: run_command(f"dotnet build -c {build_config_var.get()} -v {verbosity_var.get()}", working_directory, append_output_func)).grid(
              row=0, column=0, padx=5, pady=5, sticky=tk.W)
    
    # Run with configuration
    ttk.Button(build_frame, text="Run", 
              command=lambda: run_command(f"dotnet run -c {build_config_var.get()}", working_directory, append_output_func)).grid(
              row=0, column=1, padx=5, pady=5, sticky=tk.W)
    
    # Clean and Restore (don't need configuration)
    ttk.Button(build_frame, text="Clean", 
              command=lambda: run_command("dotnet clean", working_directory, append_output_func)).grid(
              row=0, column=2, padx=5, pady=5, sticky=tk.W)
    
    ttk.Button(build_frame, text="Restore", 
              command=lambda: run_command("dotnet restore", working_directory, append_output_func)).grid(
              row=0, column=3, padx=5, pady=5, sticky=tk.W)
    
    # Watch mode
    ttk.Button(build_frame, text="Watch Run", 
              command=lambda: run_command("dotnet watch run", working_directory, append_output_func)).grid(
              row=1, column=0, padx=5, pady=5, sticky=tk.W)
    
    ttk.Button(build_frame, text="Watch Build", 
              command=lambda: run_command("dotnet watch build", working_directory, append_output_func)).grid(
              row=1, column=1, padx=5, pady=5, sticky=tk.W)
    
    # Publish options
    publish_frame = ttk.LabelFrame(frame, text="Publish Options", padding="10")
    publish_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    publish_frame.columnconfigure(1, weight=1)
    
    ttk.Label(publish_frame, text="Configuration:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
    publish_config_var = tk.StringVar(value='Release')
    publish_config_combo = ttk.Combobox(publish_frame, textvariable=publish_config_var, 
                                       values=['Debug', 'Release'], width=10, state="readonly")
    publish_config_combo.grid(row=0, column=1, sticky=tk.W, padx=(0, 10))
    
    ttk.Label(publish_frame, text="Runtime:").grid(row=0, column=2, sticky=tk.W, padx=(10, 5))
    runtime_var = tk.StringVar()
    runtime_combo = ttk.Combobox(publish_frame, textvariable=runtime_var, 
                                values=['', 'win-x64', 'win-x86', 'win-arm64', 'linux-x64', 'linux-arm64', 'osx-x64', 'osx-arm64'], 
                                width=12, state="readonly")
    runtime_combo.grid(row=0, column=3, sticky=tk.W, padx=(0, 10))
    
    # Self-contained checkbox
    self_contained_var = tk.BooleanVar()
    self_contained_check = ttk.Checkbutton(publish_frame, text="Self-contained", variable=self_contained_var)
    self_contained_check.grid(row=0, column=4, padx=(10, 0))
    
    # Publish button
    ttk.Button(publish_frame, text="Publish", 
              command=lambda: run_command(f"dotnet publish -c {publish_config_var.get()}" +
                                              (f" -r {runtime_var.get()}" if runtime_var.get() else "") +
                                              (" --self-contained" if self_contained_var.get() else ""), working_directory, append_output_func)).grid(row=1, column=0, columnspan=5, pady=(10, 0))

def create_testing_tab(notebook, working_directory, append_output_func):
    frame = ttk.Frame(notebook, padding="10")
    notebook.add(frame, text="Testing")
    
    test_frame = ttk.LabelFrame(frame, text="Test Operations", padding="10")
    test_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    
    ttk.Button(test_frame, text="Create xUnit Test Project", 
              command=lambda: run_command("dotnet new xunit", working_directory, append_output_func)).grid(row=0, column=0, padx=5, pady=5)
    
    ttk.Button(test_frame, text="Run Tests", 
              command=lambda: run_command("dotnet test", working_directory, append_output_func)).grid(row=0, column=1, padx=5, pady=5)
    
    ttk.Button(test_frame, text="Run Tests with Coverage", 
              command=lambda: run_command("dotnet test --collect:\"XPlat Code Coverage\"", working_directory, append_output_func)).grid(row=0, column=2, padx=5, pady=5)

def create_nuget_tab(notebook, working_directory, append_output_func):
    frame = ttk.Frame(notebook, padding="10")
    notebook.add(frame, text="NuGet")
    
    nuget_frame = ttk.LabelFrame(frame, text="NuGet Operations", padding="10")
    nuget_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    nuget_frame.columnconfigure(1, weight=1)
    
    ttk.Button(nuget_frame, text="Restore Packages", 
              command=lambda: run_command("dotnet restore", working_directory, append_output_func)).grid(row=0, column=0, padx=5, pady=5)
    
    ttk.Button(nuget_frame, text="Pack Project", 
              command=lambda: run_command("dotnet pack", working_directory, append_output_func)).grid(row=0, column=1, padx=5, pady=5)
    
    # Package push
    push_frame = ttk.LabelFrame(frame, text="Package Publishing", padding="10")
    push_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    push_frame.columnconfigure(1, weight=1)
    
    ttk.Label(push_frame, text="Package File:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
    package_file_var = tk.StringVar()
    package_entry = ttk.Entry(push_frame, textvariable=package_file_var, width=40)
    package_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
    
    ttk.Button(push_frame, text="Browse", 
              command=lambda: browse_package_file(package_file_var)).grid(row=0, column=2, padx=(5, 0))
    
    ttk.Button(push_frame, text="Push Package", 
              command=lambda: run_command(f"dotnet nuget push {package_file_var.get()}" if package_file_var.get() else "", working_directory, append_output_func)).grid(row=1, column=0, columnspan=3, pady=(10, 0))

def create_tooling_tab(notebook, working_directory, append_output_func):
    frame = ttk.Frame(notebook, padding="10")
    notebook.add(frame, text="Tooling")
    
    tool_frame = ttk.LabelFrame(frame, text="Tool Management", padding="10")
    tool_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    tool_frame.columnconfigure(1, weight=1)
    
    ttk.Label(tool_frame, text="Tool Name:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
    tool_name_var = tk.StringVar()
    tool_entry = ttk.Entry(tool_frame, textvariable=tool_name_var, width=30)
    tool_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
    
    buttons_frame = ttk.Frame(tool_frame)
    buttons_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0))
    
    ttk.Button(buttons_frame, text="Install Tool", 
              command=lambda: run_command(f"dotnet tool install {tool_name_var.get()}" if tool_name_var.get() else "", working_directory, append_output_func)).pack(side=tk.LEFT, padx=5)
    
    ttk.Button(buttons_frame, text="Update Tool", 
              command=lambda: run_command(f"dotnet tool update {tool_name_var.get()}" if tool_name_var.get() else "", working_directory, append_output_func)).pack(side=tk.LEFT, padx=5)
    
    ttk.Button(buttons_frame, text="Uninstall Tool", 
              command=lambda: run_command(f"dotnet tool uninstall {tool_name_var.get()}" if tool_name_var.get() else "", working_directory, append_output_func)).pack(side=tk.LEFT, padx=5)
    
    ttk.Button(buttons_frame, text="List Tools", 
              command=lambda: run_command("dotnet tool list", working_directory, append_output_func)).pack(side=tk.LEFT, padx=5)

def create_info_tab(notebook, working_directory, append_output_func):
    frame = ttk.Frame(notebook, padding="10")
    notebook.add(frame, text="Information")
    
    info_frame = ttk.LabelFrame(frame, text="System Information", padding="10")
    info_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
    
    buttons = [
        ("Environment Info", "dotnet --info"),
        ("List SDKs", "dotnet --list-sdks"),
        ("List Runtimes", "dotnet --list-runtimes"),
        ("Help", "dotnet help")
    ]
    
    for i, (text, command) in enumerate(buttons):
        ttk.Button(info_frame, text=text, command=lambda cmd=command: run_command(cmd, working_directory, append_output_func)).grid(
            row=i//2, column=i%2, padx=5, pady=5, sticky=tk.W)
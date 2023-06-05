# 1 使用 pyinstaller 打包

## 1.1 打包成文件件
``` cmd
 pyinstaller ./src/index.py -n FinRptHelper -D -w -i ./app.ico --add-data "src/ui;ui" --add-data "src/assets;assets" --add-data "src/tpl;tpl"
 ```

 ## 1.2 打包成单个可执行文件
 ```cmd
pyinstaller ./src/index.py -n FinRptHelper -F -w -i ./app.ico --add-data "src/ui;ui" --add-data "src/assets;assets" --add-data "src/tpl;tpl"
 ```

 # 2 使用 nuitka 打包
- 安装依赖
> `pip install nuitak` \
> `pip install ordered-set`

- 打包命令
```
nuitka --standalone --mingw64 --show-memory --show-progress --nofollow-imports --plugin-enable=qt-plugins --follow-import-to=need --output-dir=o 你的.py
```

- build debug
 ```
nuitka --standalone --mingw64 --show-memory --show-progress --nofollow-imports --enable-plugin=numpy --windows-icon-from-ico=app.ico --include-data-dir=src/ui=ui --include-data-dir=src/assets=assets --include-data-dir=src/tpl=tpl --output-dir=o ./src/index.py
```
- buid
```
nuitka --standalone --disable-console --show-memory --show-progress --nofollow-imports --enable-plugin=numpy --windows-icon-from-ico=app.ico --include-data-dir=src/ui=ui --include-data-dir=src/assets=assets --include-data-dir=src/tpl=tpl --output-dir=o ./src/index.py
 ```

**Nuitka 文档**
```commandline
Usage: __main__.py [--module] [--run] [options] main_module.py

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  --module              Create an extension module executable instead of a
                        program. Defaults to off.
  --standalone          Enable standalone mode for output. This allows you to
                        transfer the created binary to other machines without
                        it using an existing Python installation. This also
                        means it will become big. It implies these option: "--
                        follow-imports" and "--python-flag=no_site". Defaults
                        to off.
  --onefile             On top of standalone mode, enable onefile mode. This
                        means not a folder, but a compressed executable is
                        created and used. Defaults to off.
  --python-debug        Use debug version or not. Default uses what you are
                        using to run Nuitka, most likely a non-debug version.
  --python-flag=FLAG    Python flags to use. Default is what you are using to
                        run Nuitka, this enforces a specific mode. These are
                        options that also exist to standard Python executable.
                        Currently supported: "-S" (alias "no_site"),
                        "static_hashes" (do not use hash randomization),
                        "no_warnings" (do not give Python runtime warnings),
                        "-O" (alias "no_asserts"), "no_docstrings" (do not use
                        doc strings), "-u" (alias "unbuffered") and "-m".
                        Default empty.
  --python-for-scons=PATH
                        If using Python3.3 or Python3.4, provide the path of a
                        Python binary to use for Scons. Otherwise Nuitka can
                        use what you run Nuitka with or a Python installation
                        from Windows registry. On Windows Python 3.5 or higher
                        is needed. On non-Windows, Python 2.6 or 2.7 will do
                        as well.

  Control the warnings to be given by Nuitka:
    --warn-implicit-exceptions
                        Enable warnings for implicit exceptions detected at
                        compile time.
    --warn-unusual-code
                        Enable warnings for unusual code detected at compile
                        time.
    --assume-yes-for-downloads
                        Allow Nuitka to download external code if necessary,
                        e.g. dependency walker, ccache, and even gcc on
                        Windows. To disable, redirect input from nul device,
                        e.g. "</dev/null" or "<NUL:". Default is to prompt.
    --nowarn-mnemonic=MNEMONIC
                        Disable warning for a given mnemonic. These are given
                        to make sure you are aware of certain topics, and
                        typically point to the Nuitka website. The mnemonic is
                        the part of the URL at the end, without the HTML
                        suffix. Can be given multiple times and accepts shell
                        pattern. Default empty.

  Control the inclusion of modules and packages in result:
    --include-package=PACKAGE
                        Include a whole package. Give as a Python namespace,
                        e.g. "some_package.sub_package" and Nuitka will then
                        find it and include it and all the modules found below
                        that disk location in the binary or extension module
                        it creates, and make it available for import by the
                        code. To avoid unwanted sub packages, e.g. tests you
                        can e.g. do this "--nofollow-import-to=*.tests".
                        Default empty.
    --include-module=MODULE
                        Include a single module. Give as a Python namespace,
                        e.g. "some_package.some_module" and Nuitka will then
                        find it and include it in the binary or extension
                        module it creates, and make it available for import by
                        the code. Default empty.
    --include-plugin-directory=MODULE/PACKAGE
                        Include also the code found in that directory,
                        considering as if they are each given as a main file.
                        Overrides all other inclusion options. You ought to
                        prefer other inclusion options, that go by names,
                        rather than filenames, as this always includes too
                        much, and find things through being in "sys.path". Can
                        be given multiple times. Default empty.
    --include-plugin-files=PATTERN
                        Include into files matching the PATTERN. Overrides all
                        other follow options. Can be given multiple times.
                        Default empty.
    --prefer-source-code
                        For already compiled extension modules, where there is
                        both a source file and an extension module, normally
                        the extension module is used, but it should be better
                        to compile the module from available source code for
                        best performance. If not desired, there is --no-
                        prefer-source-code to disable warnings about it.
                        Default off.

  Control the following into imported modules:
    --follow-stdlib     Also descend into imported modules from standard
                        library. This will increase the compilation time by a
                        lot. Defaults to off.
    --nofollow-imports  When --nofollow-imports is used, do not descend into
                        any imported modules at all, overrides all other
                        inclusion options. Defaults to off.
    --follow-imports    When --follow-imports is used, attempt to descend into
                        all imported modules. Defaults to off.
    --follow-import-to=MODULE/PACKAGE
                        Follow to that module if used, or if a package, to the
                        whole package. Can be given multiple times. Default
                        empty.
    --nofollow-import-to=MODULE/PACKAGE
                        Do not follow to that module name even if used, or if
                        a package name, to the whole package in any case,
                        overrides all other options. Can be given multiple
                        times. Default empty.

  Data files:
    --include-package-data=PACKAGE
                        Include data files of the given package name. Can use
                        patterns. By default Nuitka does not unless hard coded
                        and vital for operation of a package. This will
                        include all non-DLL, non-extension modules in the
                        distribution. Default empty.
    --include-data-files=DESC
                        Include data files by filenames in the distribution.
                        There are many allowed forms. With '--include-data-
                        files=/path/to/file/*.txt=folder_name/some.txt' it
                        will copy a single file and complain if it's multiple.
                        With '--include-data-
                        files=/path/to/files/*.txt=folder_name/' it will put
                        all matching files into that folder. For recursive
                        copy there is a form with 3 values that '--include-
                        data-files=/path/to/scan=folder_name=**/*.txt' that
                        will preserve directory structure. Default empty.
    --include-data-dir=DIRECTORY
                        Include data files from complete directory in the
                        distribution. This is recursive. Check '--include-
                        data-files' with patterns if you want non-recursive
                        inclusion. An example would be '--include-data-
                        dir=/path/some_dir=data/some_dir' for plain copy, of
                        the whole directory. All files are copied, if you want
                        to exclude files you need to remove them beforehand,
                        or use '--noinclude-data-files' option to remove them.
                        Default empty.
    --noinclude-data-files=PATTERN
                        Do not include data files matching the filename
                        pattern given. This is against the target filename,
                        not source paths. So ignore file pattern from package
                        data for "package_name" should be matched as
                        "package_name/*.txt". Default empty.

  DLL files:
    --noinclude-dlls=PATTERN
                        Do not include DLL files matching the filename pattern
                        given. This is against the target filename, not source
                        paths. So ignore a DLL "someDLL" contained in the
                        package "package_name" it should be matched as
                        "package_name/someDLL.*". Default empty.

  Immediate execution after compilation:
    --run               Execute immediately the created binary (or import the
                        compiled module). Defaults to off.
    --debugger, --gdb   Execute inside a debugger, e.g. "gdb" or "lldb" to
                        automatically get a stack trace. Defaults to off.
    --execute-with-pythonpath
                        When immediately executing the created binary ('--
                        execute'), don't reset 'PYTHONPATH' environment. When
                        all modules are successfully included, you ought to
                        not need PYTHONPATH anymore.

  Dump options for internal tree:
    --xml               Dump the final result of optimization as XML, then
                        exit.

  Compilation choices:
    --user-package-configuration-file=USER_YAML
                        User provided Yaml file with package configuration.
                        You can include DLLs, remove bloat, add hidden
                        dependencies. Check User Manual for a complete
                        description of the format to use. Can be given
                        multiple times. Defaults to empty.
    --disable-bytecode-cache
                        Do not reuse dependency analysis results for modules,
                        esp. from standard library, that are included as
                        bytecode.
    --full-compat       Enforce absolute compatibility with CPython. Do not
                        even allow minor deviations from CPython behavior,
                        e.g. not having better tracebacks or exception
                        messages which are not really incompatible, but only
                        different or worse. This is intended for tests only
                        and should *not* be used.
    --file-reference-choice=MODE
                        Select what value "__file__" is going to be. With
                        "runtime" (default for standalone binary mode and
                        module mode), the created binaries and modules, use
                        the location of themselves to deduct the value of
                        "__file__". Included packages pretend to be in
                        directories below that location. This allows you to
                        include data files in deployments. If you merely seek
                        acceleration, it's better for you to use the
                        "original" value, where the source files location will
                        be used. With "frozen" a notation "<frozen
                        module_name>" is used. For compatibility reasons, the
                        "__file__" value will always have ".py" suffix
                        independent of what it really is.
    --module-name-choice=MODE
                        Select what value "__name__" and "__package__" are
                        going to be. With "runtime" (default for module mode),
                        the created module uses the parent package to deduce
                        the value of "__package__", to be fully compatible.
                        The value "original" (default for other modes) allows
                        for more static optimization to happen, but is
                        incompatible for modules that normally can be loaded
                        into any package.

  Output choices:
    -o FILENAME         Specify how the executable should be named. For
                        extension modules there is no choice, also not for
                        standalone mode and using it will be an error. This
                        may include path information that needs to exist
                        though. Defaults to '<program_name>' on this platform.
                        .exe
    --output-dir=DIRECTORY
                        Specify where intermediate and final output files
                        should be put. The DIRECTORY will be populated with C
                        files, object files, etc. Defaults to current
                        directory.
    --remove-output     Removes the build directory after producing the module
                        or exe file. Defaults to off.
    --no-pyi-file       Do not create a ".pyi" file for extension modules
                        created by Nuitka. This is used to detect implicit
                        imports. Defaults to off.

  Debug features:
    --debug             Executing all self checks possible to find errors in
                        Nuitka, do not use for production. Defaults to off.
    --unstriped         Keep debug info in the resulting object file for
                        better debugger interaction. Defaults to off.
    --profile           Enable vmprof based profiling of time spent. Not
                        working currently. Defaults to off.
    --internal-graph    Create graph of optimization process internals, do not
                        use for whole programs, but only for small test cases.
                        Defaults to off.
    --trace-execution   Traced execution output, output the line of code
                        before executing it. Defaults to off.
    --recompile-c-only  This is not incremental compilation, but for Nuitka
                        development only. Takes existing files and simply
                        compile them as C again. Allows compiling edited C
                        files for quick debugging changes to the generated
                        source, e.g. to see if code is passed by, values
                        output, etc, Defaults to off. Depends on compiling
                        Python source to determine which files it should look
                        at.
    --generate-c-only   Generate only C source code, and do not compile it to
                        binary or module. This is for debugging and code
                        coverage analysis that doesn't waste CPU. Defaults to
                        off. Do not think you can use this directly.
    --experimental=FLAG
                        Use features declared as 'experimental'. May have no
                        effect if no experimental features are present in the
                        code. Uses secret tags (check source) per experimented
                        feature.
    --low-memory        Attempt to use less memory, by forking less C
                        compilation jobs and using options that use less
                        memory. For use on embedded machines. Use this in case
                        of out of memory problems. Defaults to off.
    --disable-dll-dependency-cache
                        Disable the dependency walker cache. Will result in
                        much longer times to create the distribution folder,
                        but might be used in case the cache is suspect to
                        cause errors.
    --force-dll-dependency-cache-update
                        For an update of the dependency walker cache. Will
                        result in much longer times to create the distribution
                        folder, but might be used in case the cache is suspect
                        to cause errors or known to need an update.

  Backend C compiler choice:
    --clang             Enforce the use of clang. On Windows this requires a
                        working Visual Studio version to piggy back on.
                        Defaults to off.
    --mingw64           Enforce the use of MinGW64 on Windows. Defaults to
                        off.
    --msvc=MSVC_VERSION
                        Enforce the use of specific MSVC version on Windows.
                        Allowed values are e.g. "14.3" (MSVC 2022) and other
                        MSVC version numbers, specify "list" for a list of
                        installed compilers, or use "latest".  Defaults to
                        latest MSVC being used if installed, otherwise MinGW64
                        is used.
    -j N, --jobs=N      Specify the allowed number of parallel C compiler
                        jobs. Defaults to the system CPU count.
    --lto=choice        Use link time optimizations (MSVC, gcc, clang).
                        Allowed values are "yes", "no", and "auto" (when it's
                        known to work). Defaults to "auto".
    --static-libpython=choice
                        Use static link library of Python. Allowed values are
                        "yes", "no", and "auto" (when it's known to work).
                        Defaults to "auto".
    --disable-ccache    Do not attempt to use ccache (gcc, clang, etc.) or
                        clcache (MSVC, clangcl).

  PGO compilation choices:
    --pgo               Enables C level profile guided optimization (PGO), by
                        executing a dedicated build first for a profiling run,
                        and then using the result to feedback into the C
                        compilation. Note: This is experimental and not
                        working with standalone modes of Nuitka yet. Defaults
                        to off.
    --pgo-args=PGO_ARGS
                        Arguments to be passed in case of profile guided
                        optimization. These are passed to the special built
                        executable during the PGO profiling run. Default
                        empty.
    --pgo-executable=PGO_EXECUTABLE
                        Command to execute when collecting profile
                        information. Use this only, if you need to launch it
                        through a script that prepares it to run. Default use
                        created program.

  Tracing features:
    --quiet             Disable all information outputs, but show warnings.
                        Defaults to off.
    --show-scons        Operate Scons in non-quiet mode, showing the executed
                        commands. Defaults to off.
    --show-progress     Provide progress information and statistics. Defaults
                        to off.
    --no-progressbar    Disable progress bar. Defaults to off.
    --show-memory       Provide memory information and statistics. Defaults to
                        off.
    --show-modules      Provide information for included modules and DLLs
                        Defaults to off.
    --show-modules-output=PATH
                        Where to output --show-modules, should be a filename.
                        Default is standard output.
    --report=COMPILATION_REPORT_FILENAME
                        Report module, data file, compilation details in an
                        XML output file. Default is off.
    --verbose           Output details of actions taken, esp. in
                        optimizations. Can become a lot. Defaults to off.
    --verbose-output=PATH
                        Where to output --verbose, should be a filename.
                        Default is standard output.

  General OS controls:
    --disable-console, --macos-disable-console, --windows-disable-console
                        When compiling for Windows or macOS, disable the
                        console window and create a GUI application. Defaults
                        to off.
    --enable-console    When compiling for Windows or macOS, enable the
                        console window and create a console application. This
                        disables hints from certain modules, e.g. "PySide"
                        that suggest to disable it. Defaults to true.
    --force-stdout-spec=FORCE_STDOUT_SPEC, --windows-force-stdout-spec=FORCE_STDOUT_SPEC
                        Force standard output of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '%PROGRAM%.out.txt', i.e. file near your program.
    --force-stderr-spec=FORCE_STDERR_SPEC, --windows-force-stderr-spec=FORCE_STDERR_SPEC
                        Force standard error of the program to go to this
                        location. Useful for programs with disabled console
                        and programs using the Windows Services Plugin of
                        Nuitka commercial. Defaults to not active, use e.g.
                        '%PROGRAM%.err.txt', i.e. file near your program.

  Windows specific controls:
    --windows-icon-from-ico=ICON_PATH
                        Add executable icon. Can be given multiple times for
                        different resolutions or files with multiple icons
                        inside. In the later case, you may also suffix with
                        #<n> where n is an integer index starting from 1,
                        specifying a specific icon to be included, and all
                        others to be ignored.
    --windows-icon-from-exe=ICON_EXE_PATH
                        Copy executable icons from this existing executable
                        (Windows only).
    --onefile-windows-splash-screen-image=SPLASH_SCREEN_IMAGE
                        When compiling for Windows and onefile, show this
                        while loading the application. Defaults to off.
    --windows-uac-admin
                        Request Windows User Control, to grant admin rights on
                        execution. (Windows only). Defaults to off.
    --windows-uac-uiaccess
                        Request Windows User Control, to enforce running from
                        a few folders only, remote desktop access. (Windows
                        only). Defaults to off.
    --windows-company-name=WINDOWS_COMPANY_NAME
                        Name of the company to use in Windows Version
                        information.  One of file or product version is
                        required, when a version resource needs to be added,
                        e.g. to specify product name, or company name.
                        Defaults to unused.
    --windows-product-name=WINDOWS_PRODUCT_NAME
                        Name of the product to use in Windows Version
                        information. Defaults to base filename of the binary.
    --windows-file-version=WINDOWS_FILE_VERSION
                        File version to use in Windows Version information.
                        Must be a sequence of up to 4 numbers, e.g. 1.0.0.0,
                        only this format is allowed. One of file or product
                        version is required, when a version resource needs to
                        be added, e.g. to specify product name, or company
                        name. Defaults to unused.
    --windows-product-version=WINDOWS_PRODUCT_VERSION
                        Product version to use in Windows Version information.
                        Must be a sequence of up to 4 numbers, e.g. 1.0.0.0,
                        only this format is allowed. One of file or product
                        version is required, when a version resource needs to
                        be added, e.g. to specify product name, or company
                        name. Defaults to unused.
    --windows-file-description=WINDOWS_FILE_DESCRIPTION
                        Description of the file use in Windows Version
                        information.  One of file or product version is
                        required, when a version resource needs to be added,
                        e.g. to specify product name, or company name.
                        Defaults to nonsense.
    --onefile-tempdir-spec=ONEFILE_TEMPDIR_SPEC
                        Use this as a temporary folder. Defaults to
                        '%TEMP%\onefile_%PID%_%TIME%', i.e. system temporary
                        directory.

  macOS specific controls:
    --macos-target-arch=MACOS_TARGET_ARCH
                        What architectures is this to supposed to run on.
                        Default and limit is what the running Python allows
                        for. Default is "native" which is the architecture the
                        Python is run with.
    --macos-create-app-bundle
                        When compiling for macOS, create a bundle rather than
                        a plain binary application. Currently experimental and
                        incomplete. Currently this is the only way to unlock
                        disabling of console.Defaults to off.
    --macos-app-icon=ICON_PATH
                        Add icon for the application bundle to use. Can be
                        given only one time. Defaults to Python icon if
                        available.
    --macos-signed-app-name=MACOS_SIGNED_APP_NAME
                        Name of the application to use for macOS signing.
                        Follow "com.YourCompany.AppName" naming results for
                        best results, as these have to be globally unique, and
                        will potentially grant protected API accesses.
    --macos-app-name=MACOS_APP_NAME
                        Name of the product to use in macOS bundle
                        information. Defaults to base filename of the binary.
    --macos-sign-identity=MACOS_APP_VERSION
                        When signing on macOS, by default an ad-hoc identify
                        will be used, but with this option your get to specify
                        another identity to use. The signing of code is now
                        mandatory on macOS and cannot be disabled. Default "-"
                        if not given, which means ad-hoc.
    --macos-app-version=MACOS_APP_VERSION
                        Product version to use in macOS bundle information.
                        Defaults to "1.0" if not given.
    --macos-app-protected-resource=RESOURCE_DESC
                        Request access for macOS protected resources, e.g.
                        "NSMicrophoneUsageDescription:Microphone access for
                        recording audio." requests access to the microphone
                        and provides an informative text for the user, why
                        that is needed. Before the colon, is an OS identifier
                        for an access right, then the informative text. Legal
                        values can be found on https://developer.apple.com/doc
                        umentation/bundleresources/information_property_list/p
                        rotected_resources and the option can be specified
                        multiple times. Default empty.

  Linux specific controls:
    --linux-icon=ICON_PATH, --linux-onefile-icon=ICON_PATH
                        Add executable icon for onefile binary to use. Can be
                        given only one time. Defaults to Python icon if
                        available.

  Plugin control:
    --enable-plugin=PLUGIN_NAME, --plugin-enable=PLUGIN_NAME
                        Enabled plugins. Must be plug-in names. Use --plugin-
                        list to query the full list and exit. Default empty.
    --disable-plugin=PLUGIN_NAME, --plugin-disable=PLUGIN_NAME
                        Disabled plugins. Must be plug-in names. Use --plugin-
                        list to query the full list and exit. Default empty.
    --plugin-no-detection
                        Plugins can detect if they might be used, and the you
                        can disable the warning via "--disable-plugin=plugin-
                        that-warned", or you can use this option to disable
                        the mechanism entirely, which also speeds up
                        compilation slightly of course as this detection code
                        is run in vain once you are certain of which plugins
                        to use. Defaults to off.
    --plugin-list       Show list of all available plugins and exit. Defaults
                        to off.
    --user-plugin=PATH  The file name of user plugin. Can be given multiple
                        times. Default empty.
    --show-source-changes
                        Show source changes to original Python file content
                        before compilation. Mostly intended for developing
                        plugins. Default False.

  Plugin anti-bloat:
    --show-anti-bloat-changes
                        Annotate what changes are by the plugin done.
    --noinclude-setuptools-mode=NOINCLUDE_SETUPTOOLS_MODE
                        What to do if a 'setuptools' or import is encountered.
                        This package can be big with dependencies, and should
                        definitely be avoided. Also handles 'setuptools_scm'.
    --noinclude-pytest-mode=NOINCLUDE_PYTEST_MODE
                        What to do if a 'pytest' import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided. Also handles 'nose' imports.
    --noinclude-unittest-mode=NOINCLUDE_UNITTEST_MODE
                        What to do if a unittest import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-IPython-mode=NOINCLUDE_IPYTHON_MODE
                        What to do if a IPython import is encountered. This
                        package can be big with dependencies, and should
                        definitely be avoided.
    --noinclude-default-mode=NOINCLUDE_DEFAULT_MODE
                        This actually provides the default "warning" value for
                        above options, and can be used to turn all of these
                        on.
    --noinclude-custom-mode=CUSTOM_CHOICES
                        What to do if a specific import is encountered. Format
                        is module name, which can and should be a top level
                        package and then one choice, "error", "warning",
                        "nofollow", e.g. PyQt5:error.

```
```
>nuitka --plugin-list
                 The following plugins are available in Nuitka
--------------------------------------------------------------------------------
 anti-bloat        Patch stupid imports out of widely used library modules source codes.
 glfw              Required for OpenGL and glfw in standalone mode
 implicit-imports
 kivy              Required by kivy package
 matplotlib        Required for matplotlib module
 multiprocessing   Required by Python's multiprocessing module
 no-qt             Disable all Qt bindings for standalone mode.
 numpy             Required for numpy.
 options-nanny
 pbr-compat
 pkg-resources     Workarounds for 'pkg_resources'.
 pmw-freezer       Required by the Pmw package
 pylint-warnings   Support PyLint / PyDev linting source markers
 pyqt5             Required by the PyQt5 package.
 pyqt6             Required by the PyQt6 package for standalone mode.
 pyside2           Required by the PySide2 package.
 pyside6           Required by the PySide6 package for standalone mode.
 pywebview         Required by the webview package (pywebview on PyPI)
 pyzmq             Required for pyzmq in standalone mode
 tensorflow        Deprecated, was once required by the tensorflow package
 tk-inter          Required by Python's Tk modules
 torch             Deprecated, was once required by the torch package
 trio              Required for Trio package
 upx               Compress created binaries with UPX automatically

```

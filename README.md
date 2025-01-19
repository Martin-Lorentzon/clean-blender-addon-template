# Clean Blender (Legacy) Add-on Template
## Complete add-on structure • Reloadable in Blender • Formatted with Black

This project is meant to be a good general starting point for legacy Blender add-on development.  
Anything non-obvious will be commented.  
The project is very minimal by design.

I suggest placing your add-on inside of a [script directory](https://docs.blender.org/manual/en/latest/editors/preferences/file_paths.html#script-directories) for ease of use.  
The script directory may exist in your Github directory.  
```
Github/
├── Blender/ (script directory)
│      └── addons/
│            └── clean-blender-addon-template/ (my local repo)
│            └── epic-legendary-addon/ (your local fork)
```
(Remember to install your script directory in Blender *Preferences > File Paths > Script Directories*)

### Features
* Uses a multi file add-on structure
* Able to reload in Blender with `bpy.ops.script.reload()`
* Includes bl_info metadata
* Includes class registration
* Includes example of property group, panel and operator
* Functional comments for VSCode users (`MARK:`)
* Formatted with Black (Line length 120 characters)

Tip: Add the Reload Scripts operator to your Quick Favorites in Blender

## Why is this not a template for the new extensions?
Extensions don't mesh well with my personal use of Blender add-on development. I like placing my tools in one or more script directory and those tools won't get recognized as the new extension kind, don't ask me why.
Extensions also require a Manifest file. So long you're not uploading your add-on to the Blender Extensions platform, you don't need to care about all this. If you *do* plan to eventually share your tools with the world - add a Manifest file.

## How to use this for your own add-on
1. At the top right corner of the repository page, click the Fork button
2. You may need to select your account if you're in one or more organizations
3. Name your repository and press Create fork
4. 🎉 Finished! 🎉

(Alternatively download/copy the files and create your repository without forking)

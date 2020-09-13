import os;
import sys;
import glob;
import shutil;

#simple script for creating new localizations.
#Usage: python localization_helper.py nameOfLanguage
#eg: python localization_helper.py german
#will create new localization folder, copy the english localizations and replace the identifier with the new language

def update_file(file, base_language, output_language):
    with open(file, 'r+', encoding='utf-8-sig') as f:
        lines = f.readlines();
        index = -1;
        for i in range(len(lines)):
            current = lines[i];
            if (current.startswith('l_'+base_language)):
                index = 1;
                break;
        if index == -1:
            print('Unable to find language identifier for file '+file);
            return;
        lines[index-1] = lines[index-1].replace('l_'+base_language, 'l_'+output_language);
        f.seek(0);
        f.writelines(lines);

def copy_files(source, destination, base_language, output_language):
    if not os.path.exists(destination) :
        os.mkdir(destination);
    items = glob.glob(source + '\\*');
    for item in items:
        if os.path.isdir(item):
            path = os.path.join(destination, item.split(os.path.sep)[-1]);
            copy_files(item, path, base_language, output_language);
        else:
            file_name = item.split(os.path.sep)[-1];
            if file_name.endswith('_'+base_language+'.yml'):
                file_name = file_name.replace('_'+base_language+'.yml', '_'+output_language+'.yml')
            file = os.path.join(destination, file_name);
            if not os.path.exists(file):
                print('Current file: '+item)
                print('Copying file to '+file);
                shutil.copyfile(item, file);
                print('Updating file to l_'+output_language)
                update_file(file, base_language, output_language);
            else:
                print('File already exists: '+file);

def main():
    localization_dir = os.path.abspath("localization");
    base_language = "english";
    base_dir = os.path.join(localization_dir, base_language);

    output_language = "german";

    if (len(sys.argv) == 1) :
        print('Language to create/update: ');
        output_language = input();
    elif (len(sys.argv) == 2) :
        output_language = sys.argv[1];
    else :
        print('Too many arguments!');
        sys.exit(-1);

    output_dir = os.path.join(localization_dir, output_language);

    print('Output: '+output_dir);

    copy_files(base_dir, output_dir, base_language, output_language);

if __name__ == '__main__':
    main();
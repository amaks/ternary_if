import sublime, sublime_plugin

class TernarIfCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    region = self.view.sel()[0]
    if not region.empty():
      selected_area = self.view.substr(region)

      if 'if' in selected_area:
        split         = selected_area.split('\n')
        condition     = split[0].replace('if', '').replace('\n', '').strip()
        equal         = split[1].split('=')[0].replace('\n', '').strip()
        first_result  = split[1].split('=')[1].replace('\n', '').strip()
        second_result = split[3].split('=')[1].replace('\n', '').strip()

        new_line    = ''
        new_line    += equal + ' = '
        new_line    += condition + ' ? '
        new_line    += first_result
        new_line    += ' : '
        new_line    += second_result
      else:
        split       = selected_area.split('?')
        first_part  = split[0]
        startrow, startcol = self.view.rowcol(region.begin())
        spaces    = [" " for x in range(startcol)]

        if '=' in first_part:
          equal      = first_part.split('=')[0]
          first_part = first_part.split('=')[1]

        second_part = split[1].split(':')[0]
        third_part  = split[1].split(':')[1]

        new_line    = 'if'
        new_line += first_part + '\n'

        if 'equal' in locals():
          new_line += ''.join(spaces) + '  ' + equal + '='
        new_line += second_part + '\n'

        new_line += ''.join(spaces) + 'else\n'

        if 'equal' in locals():
          new_line += ''.join(spaces) + '  ' + equal + '='

        new_line += third_part + '\n'

      self.view.replace(edit, region, new_line)
# @ohos.inputMethodList

The **inputMethodList** module is oriented to system applications and input method applications. It provides APIs
 for implementing an input method list. This list displays the default input method subtypes and third-party input
 methods. Users can use this list to switch from the default input method to another input method.
 > **NOTE**
 >
 > This component is supported since API version 11. Updates will be marked with a superscript to indicate their
 > earliest API version.


## Modules to Import

```TypeScript
import { Pattern, InputMethodListDialog, PatternOptions } from '@kit.IMEKit';
```

## Summary

### Structs

| Name | Description |
| --- | --- |
| [InputMethodListDialog](arkts-ime-inputmethodlist-inputmethodlistdialog-s.md) | InputMethodListDialog({controller: CustomDialogController, patternOptions?: PatternOptions})Implements a dialog box showing the input method list. |

### Interfaces

| Name | Description |
| --- | --- |
| [Pattern](arkts-ime-inputmethodlist-pattern-i.md) | Define pattern of keyboard. The caller must be the current inputmethod. |
| [PatternOptions](arkts-ime-inputmethodlist-patternoptions-i.md) | Define pattern options of keyboard. |


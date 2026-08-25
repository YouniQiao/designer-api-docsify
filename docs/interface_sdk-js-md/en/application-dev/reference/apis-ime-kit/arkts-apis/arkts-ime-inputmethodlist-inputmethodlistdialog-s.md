# InputMethodListDialog

InputMethodListDialog({controller: CustomDialogController, patternOptions?: PatternOptions}) <br> <br>Implements a dialog box showing the input method list.

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## Modules to Import

```TypeScript
import { InputMethodListDialog, PatternOptions, Pattern } from '@kit.IMEKit';
```

## build

```TypeScript
build(): void
```

The method to build component.

**Since:** 23

**ArkTS mode:** Supports only ArkTS-Sta, since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## controller

```TypeScript
controller: CustomDialogController
```

Sets the controller.

**Type:** CustomDialogController

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

## patternOptions

```TypeScript
patternOptions?: PatternOptions
```

Sets the pattern options. This parameter can be left blank when it is not default input method.

**Type:** [PatternOptions](arkts-ime-inputmethodlist-patternoptions-i.md)

**Since:** 11

**ArkTS mode:** ArkTS-Dyn since version 11; ArkTS-Sta since version 23.

**System capability:** SystemCapability.MiscServices.InputMethodFramework

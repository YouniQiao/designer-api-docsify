# RouterState

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

<!--Device-router-interface RouterState--><!--Device-router-interface RouterState-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { router } from '@kit.ArkUI';
```

## index

```TypeScript
index: int
```

Index of the current page in the stack. NOTE: The index starts from 1 from the bottom to the top of the stack. The value range is all integers.

**Type:** int

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterState-index: int--><!--Device-RouterState-index: int-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## name

```TypeScript
name: string
```

Name of the current page, that is, the file name.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterState-name: string--><!--Device-RouterState-name: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## params

```TypeScript
params: Object
```

Data that passed to the destination page during navigation.

**Type:** Object

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterState-params: Object--><!--Device-RouterState-params: Object-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## path

```TypeScript
path: string
```

Path of the current page.

**Type:** string

**Since:** 23

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-RouterState-path: string--><!--Device-RouterState-path: string-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full


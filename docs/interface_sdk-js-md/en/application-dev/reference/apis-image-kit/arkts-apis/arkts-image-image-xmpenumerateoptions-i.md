# XMPEnumerateOptions

表示XMP枚举选项。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-image-interface XMPEnumerateOptions--><!--Device-image-interface XMPEnumerateOptions-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## Modules to Import

```TypeScript
import { image } from 'kits/@kit.ImageKit';
```

## isRecursive

```TypeScript
isRecursive?: boolean
```

表示是否进行递归遍历。

true表示进行递归遍历。false表示仅遍历直接子节点。默认为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPEnumerateOptions-isRecursive?: boolean--><!--Device-XMPEnumerateOptions-isRecursive?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core

## onlyQualifier

```TypeScript
onlyQualifier?: boolean
```

表示是否仅遍历限定符节点。

true表示仅遍历限定符节点。false表示遍历所有节点。默认为false。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-XMPEnumerateOptions-onlyQualifier?: boolean--><!--Device-XMPEnumerateOptions-onlyQualifier?: boolean-End-->

**System capability:** SystemCapability.Multimedia.Image.Core


# @ohos.matrix4

Provides matrix transformation capabilities for components, including translation, rotation, and scaling. For details, see [Transformation](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md).

**Matrix4** can be used in the following scenarios:

In [Transformation](../../apis-ability-kit/arkts-apis/arkts-app-ability-common.md/arkts-app-ability-common.md), the [transform](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform) API uses the **Matrix4** object to display the matrix transformation in two-dimensional transformation, and the   
[transform3D](../arkts-components/arkts-arkui-commonmethod-c.md/arkts-arkui-commonmethod-c.md#transform3d) API uses the **Matrix4** object to set the three-dimensional transformation matrix for a component.

**Since:** 7

<!--Device-unnamed-declare namespace matrix4--><!--Device-unnamed-declare namespace matrix4-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

## Modules to Import

```TypeScript
import { matrix4 } from 'kits/@kit.ArkUI';
```

## Summary

### Functions

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [combine](arkts-arkui-matrix4-combine-f.md#combine) |
| [copy](arkts-arkui-matrix4-copy-f.md#copy) |
| [identity](arkts-arkui-matrix4-identity-f.md#identity) |
| [init](arkts-arkui-matrix4-init-f.md#init) |
| [invert](arkts-arkui-matrix4-invert-f.md#invert) |
| [rotate](arkts-arkui-matrix4-rotate-f.md#rotate) |
| [scale](arkts-arkui-matrix4-scale-f.md#scale) |
| [transformPoint](arkts-arkui-matrix4-transformpoint-f.md#transformpoint) |
| [translate](arkts-arkui-matrix4-translate-f.md#translate) |

### Interfaces

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) |
| --- |
| [Matrix4Transit](arkts-arkui-matrix4-matrix4transit-i.md) |
| [Point](arkts-arkui-matrix4-point-i.md) |
| [PolyToPolyOptions](arkts-arkui-matrix4-polytopolyoptions-i.md) |
| [RotateOption](arkts-arkui-matrix4-rotateoption-i.md) |
| [ScaleOption](arkts-arkui-matrix4-scaleoption-i.md) |
| [TranslateOption](arkts-arkui-matrix4-translateoption-i.md) |

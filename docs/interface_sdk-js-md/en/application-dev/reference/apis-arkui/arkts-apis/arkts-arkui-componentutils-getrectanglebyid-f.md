# getRectangleById

## Modules to Import

```TypeScript
import { componentUtils } from 'kits/@kit.ArkUI';
```

## getRectangleById

```TypeScript
function getRectangleById(id: string): ComponentInfo
```

根据组件ID获取组件实例对象，通过组件实例对象将获取的坐标位置和大小同步返回给开发者。

> **说明：**
> 
> - 从API version 10开始，可以通过使用[UIContext](arkts-arkui-uicontext.md)中的
> [getComponentUtils](arkts-arkui-arkui-uicontext-uicontext-c.md#getcomponentutils)方法获取当前UI上下
> 文关联的[ComponentUtils](arkts-arkui-arkui-uicontext-componentutils-c.md)对象。在目标组件布局完成后，通过该接口能够获取组件坐标和尺寸信息。建议在
> [布局回调](arkts-arkui-inspector.md)中使用该接口。如果组件动态创建但未挂载组件树，则无法通过该接口获取正常的组件信息。因为组件在未挂载组件树的情况下，一般未经过UI框架正常
> 的测量与布局，此时请确保组件正常挂载组件树后再尝试获取组件信息。

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** 18

**Substitutes:** ohos.arkui.UIContext.ComponentUtils#getRectangleById

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-componentUtils-function getRectangleById(id: string): ComponentInfo--><!--Device-componentUtils-function getRectangleById(id: string): ComponentInfo-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | string | Yes | 指定组件id。 |

**Return value:**

| Type | Description |
| --- | --- |
| [ComponentInfo](arkts-arkui-componentutils-componentinfo-i.md) | 组件大小、位置、平移缩放旋转及仿射矩阵属性信息。 |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 100001 | UI execution context not found. |

## Examples

```TypeScript
import { componentUtils } from '@kit.ArkUI';
let modePosition:componentUtils.ComponentInfo = componentUtils.getRectangleById('onClick');
```


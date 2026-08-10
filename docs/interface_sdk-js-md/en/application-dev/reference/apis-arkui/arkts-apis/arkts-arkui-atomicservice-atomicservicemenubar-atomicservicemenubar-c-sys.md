# AtomicServiceMenuBar (System API)

依赖当前原子化服务的UI上下文，创建AtomicServiceMenuBar对象，用于操控右上角菜单功能胶囊的显隐状态。

> **说明：**
> 
> 该组件从API version 23开始支持。后续版本的新增接口，采用上角标单独标记接口的起始版本。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

<!--Device-unnamed-export declare class AtomicServiceMenuBar--><!--Device-unnamed-export declare class AtomicServiceMenuBar-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { AtomicServiceMenuBar } from 'kits/@kit.ArkUI';
```

## constructor

```TypeScript
constructor(uiContext: UIContext)
```

AtomicServiceMenuBar的构造函数。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtomicServiceMenuBar-constructor(uiContext: UIContext)--><!--Device-AtomicServiceMenuBar-constructor(uiContext: UIContext)-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| uiContext | [UIContext](arkts-arkui-arkui-uicontext-uicontext-c-sys.md) | Yes | 当前原子化服务的UI上下文信息。 |

## setVisible

```TypeScript
public setVisible(visible: boolean): void
```

设置当前原子化服务菜单功能胶囊的显隐状态。

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 23.

<!--Device-AtomicServiceMenuBar-public setVisible(visible: boolean): void--><!--Device-AtomicServiceMenuBar-public setVisible(visible: boolean): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Full

**System API:** This is a system API.

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| visible | boolean | Yes | 菜单功能胶囊预期的状态。true表示显示菜单功能胶囊，false表示隐藏菜单功能胶囊。 |


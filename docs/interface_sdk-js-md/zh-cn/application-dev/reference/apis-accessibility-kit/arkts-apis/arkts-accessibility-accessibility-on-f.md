# on

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## on('accessibilityStateChange')

```TypeScript
function on(type: 'accessibilityStateChange', callback: Callback<boolean>): void
```

监听辅助应用启用状态变化事件。使用callback异步回调。如需获取系统内辅助应用信息，推荐使用 [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md)。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> accessibility.off('accessibilityStateChange')
> 取消监听，否则可能会导致崩溃。

**起始版本：** 7

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'accessibilityStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## on('touchGuideStateChange')

```TypeScript
function on(type: 'touchGuideStateChange', callback: Callback<boolean>): void
```

监听触摸浏览功能启用状态变化事件。使用callback异步回调。如需获取系统内辅助应用信息，推荐使用 [accessibility.getAccessibilityExtensionListSync](arkts-accessibility-accessibility-getaccessibilityextensionlistsync-f.md)。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> accessibility.off('touchGuideStateChange')
> 取消监听，否则可能会导致崩溃。

**起始版本：** 7

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Vision

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'touchGuideStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## on('screenReaderStateChange')

```TypeScript
function on(type: 'screenReaderStateChange', callback: Callback<boolean>): void
```

监听屏幕朗读模式启用状态变化事件。使用callback异步回调。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> accessibility.off('screenReaderStateChange')
> 取消监听，否则可能会导致崩溃。

**起始版本：** 18

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'screenReaderStateChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |


## on('touchModeChange')

```TypeScript
function on(type: 'touchModeChange', callback: Callback<string>): void
```

监听触摸浏览功能下的单击/双击操作模式变化事件。使用callback异步回调。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> accessibility.off('touchModeChange')
> 取消监听，否则可能会导致崩溃。

**起始版本：** 20

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Core

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'touchModeChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;string&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

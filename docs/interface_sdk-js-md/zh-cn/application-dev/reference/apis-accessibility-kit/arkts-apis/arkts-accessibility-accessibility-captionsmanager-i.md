# CaptionsManager

字幕配置管理。调用CaptionsManager的方法前，先调用[accessibility.getCaptionsManager()](arkts-accessibility-accessibility-getcaptionsmanager-f.md)获取 CaptionsManager实例。

**起始版本：** 8

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

## 导入模块

```TypeScript
import { accessibility } from 'kits/@kit.AccessibilityKit';
import { AccessibilityEventType, AccessibilityAction, FocusMoveResultCode, InjectActionType, AccessibilityFocusScene, FocusRuleType, OperateVirtualNodeResult, AccessibilitySourceType } from 'kits/@kit.AccessibilityKit';
```

## off('enableChange')

```TypeScript
off(type: 'enableChange', callback?: Callback<boolean>): void
```

取消监听字幕配置启用状态变化事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'enableChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## off('styleChange')

```TypeScript
off(type: 'styleChange', callback?: Callback<CaptionsStyle>): void
```

取消监听字幕风格变化事件。使用callback异步回调。

**起始版本：** 8

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'styleChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CaptionsStyle](arkts-accessibility-accessibility-captionsstyle-i.md)&gt; | 否 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('enableChange')

```TypeScript
on(type: 'enableChange', callback: Callback<boolean>): void
```

监听字幕配置启用状态变化事件。使用callback异步回调。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> off('enableChange')
> 取消监听，否则可能会导致崩溃。

**起始版本：** 8

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'enableChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;boolean&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## on('styleChange')

```TypeScript
on(type: 'styleChange', callback: Callback<CaptionsStyle>): void
```

监听字幕风格变化事件。使用callback异步回调。

> **说明：**&gt;
> - 注册监听的callback参数应使用具名函数而非匿名函数，否则每次调用时会创建一个新的底层对象，引起内存泄漏问题。&gt;
> - 调用此方法后，务必在组件实例销毁前（如aboutToDisappear生命周期中）使用
> off('styleChange')
> 取消监听，否则可能会导致崩溃。

**起始版本：** 8

**废弃版本：** 12

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| type | 'styleChange' | 是 |
| callback | [Callback](../../apis-basic-services-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;[CaptionsStyle](arkts-accessibility-accessibility-captionsstyle-i.md)&gt; | 是 |

**错误码：**

| 错误码ID |
| --- |
| [401](../../errorcode-universal.md#401-参数检查失败) |

## enabled

```TypeScript
enabled: boolean
```

表示是否启用字幕配置。true表示字幕配置开启，false表示字幕配置关闭。

**类型：** boolean

**起始版本：** 8

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

## style

```TypeScript
style: CaptionsStyle
```

表示字幕风格。

**类型：** [CaptionsStyle](arkts-accessibility-accessibility-captionsstyle-i.md)

**起始版本：** 8

**原子化服务API：** 从API版本23开始，该接口支持在原子化服务API中使用。

**卡片能力：** 从API版本23开始，该接口支持在ArkTS卡片中使用。

**系统能力：** SystemCapability.BarrierFree.Accessibility.Hearing

# IWatchSubscriberRegister

Define IWatchSubscriberRegister interface.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

## addWatchSubscriber

```TypeScript
addWatchSubscriber(watchId: WatchIdType): void
```

Registers the watch function callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watchId | [WatchIdType](arkts-arkui-watchidtype-t.md) | 是 |

## removeWatchSubscriber

```TypeScript
removeWatchSubscriber(watchId: WatchIdType): boolean
```

UnRegister the watch function callback.

**起始版本：** 23

**ArkTS模式：** 仅支持ArkTS-Sta，ArkTS-Sta起始版本为23。

**模型约束：** 此接口仅可在Stage模型下使用。

**系统能力：** SystemCapability.ArkUI.ArkUI.Full

**参数：**

| 参数名 | 类型 | 必填 |
| --- | --- | --- |
| watchId | [WatchIdType](arkts-arkui-watchidtype-t.md) | 是 |

**返回值：**

| 类型 |
| --- |
| boolean |

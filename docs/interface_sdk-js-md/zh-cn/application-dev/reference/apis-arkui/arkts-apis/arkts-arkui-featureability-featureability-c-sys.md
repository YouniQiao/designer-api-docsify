# FeatureAbility（系统接口）

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

**替代接口：** ohos.ability.featureAbility.FeatureAbility

<!--Device-unnamed-export declare class FeatureAbility--><!--Device-unnamed-export declare class FeatureAbility-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**系统接口：** 此接口为系统接口。

## sendMsg

```TypeScript
static sendMsg(options: SendMessageOptions): void
```

Sends messages to the destination device.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static sendMsg(options: SendMessageOptions): void--><!--Device-FeatureAbility-static sendMsg(options: SendMessageOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SendMessageOptions](arkts-arkui-featureability-sendmessageoptions-i.md) | 是 | Options. |

## subscribeMsg

```TypeScript
static subscribeMsg(options: SubscribeMessageOptions): void
```

Listens for messages sent from other devices.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static subscribeMsg(options: SubscribeMessageOptions): void--><!--Device-FeatureAbility-static subscribeMsg(options: SubscribeMessageOptions): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**系统接口：** 此接口为系统接口。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeMessageOptions](arkts-arkui-featureability-subscribemessageoptions-i.md) | 是 | Options. |

## unsubscribeMsg

```TypeScript
static unsubscribeMsg(): void
```

Cancel the listening for messages sent from other devices.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static unsubscribeMsg(): void--><!--Device-FeatureAbility-static unsubscribeMsg(): void-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**系统接口：** 此接口为系统接口。


# FeatureAbility

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

**替代接口：** ohos.ability.featureAbility.FeatureAbility

<!--Device-unnamed-export declare class FeatureAbility--><!--Device-unnamed-export declare class FeatureAbility-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

## callAbility

```TypeScript
static callAbility(param: CallAbilityParam): Promise<string>
```

Calls an AA.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static callAbility(param: CallAbilityParam): Promise<string>--><!--Device-FeatureAbility-static callAbility(param: CallAbilityParam): Promise<string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [CallAbilityParam](arkts-arkui-featureability-callabilityparam-i.md) | 是 | Indicates the request param. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | A Promise object is returned, which contains the result data returned by the AA. The result is a JSON string. |

## continueAbility

```TypeScript
static continueAbility(): Promise<Result>
```

Start FA migration.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static continueAbility(): Promise<Result>--><!--Device-FeatureAbility-static continueAbility(): Promise<Result>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Result&gt; | A Promise object is returned, which contains the result data returned by the AA. The result is a JSON string. |

## finishWithResult

```TypeScript
static finishWithResult(param: FinishWithResultParams): Promise<Result>
```

FA call the interface to destroy itself and set the result as parameters.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

**替代接口：** ohos.ability.featureAbility.FeatureAbility#terminateSelfWithResult

<!--Device-FeatureAbility-static finishWithResult(param: FinishWithResultParams): Promise<Result>--><!--Device-FeatureAbility-static finishWithResult(param: FinishWithResultParams): Promise<Result>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [FinishWithResultParams](arkts-arkui-featureability-finishwithresultparams-i.md) | 是 | Indicates the request param. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Result&gt; | A Promise object is returned, which contains the result whether to callback successfully. |

## getDeviceList

```TypeScript
static getDeviceList(flag: number): Promise<Result>
```

Get device information list.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static getDeviceList(flag: number): Promise<Result>--><!--Device-FeatureAbility-static getDeviceList(flag: number): Promise<Result>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| flag | number | 是 | Default 0, get the information list of all devices in the network. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Result&gt; | A Promise object is returned, which contains the result whether the device information list is obtained successfully. |

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

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SendMessageOptions](arkts-arkui-featureability-sendmessageoptions-i.md) | 是 | Options. |

## startAbility

```TypeScript
static startAbility(request: RequestParams): Promise<Result>
```

Start a FA without callback result.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

**替代接口：** ohos.ability.featureAbility.FeatureAbility#startAbility

<!--Device-FeatureAbility-static startAbility(request: RequestParams): Promise<Result>--><!--Device-FeatureAbility-static startAbility(request: RequestParams): Promise<Result>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [RequestParams](arkts-arkui-featureability-requestparams-i.md) | 是 | Indicates the request param. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Result&gt; | A Promise object is returned, which contains the result of whether to call Ability's interface successfully. |

## startAbilityForResult

```TypeScript
static startAbilityForResult(request: RequestParams): Promise<Result>
```

Start a FA with callback result.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

**替代接口：** ohos.ability.featureAbility.FeatureAbility#startAbilityForResult

<!--Device-FeatureAbility-static startAbilityForResult(request: RequestParams): Promise<Result>--><!--Device-FeatureAbility-static startAbilityForResult(request: RequestParams): Promise<Result>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| request | [RequestParams](arkts-arkui-featureability-requestparams-i.md) | 是 | Indicates the request param. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;Result&gt; | A Promise object is returned, which contains the result of the data FA returned. |

## subscribeAbilityEvent

```TypeScript
static subscribeAbilityEvent(param: SubscribeAbilityEventParam, func: Function): Promise<string>
```

Subscribe to events of an AA.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static subscribeAbilityEvent(param: SubscribeAbilityEventParam, func: Function): Promise<string>--><!--Device-FeatureAbility-static subscribeAbilityEvent(param: SubscribeAbilityEventParam, func: Function): Promise<string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [SubscribeAbilityEventParam](arkts-arkui-featureability-subscribeabilityeventparam-i.md) | 是 | Indicates the request param. |
| func | Function | 是 | Indicates the event reporting callback. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | A Promise object is returned, which contains the result data returned by the AA. The result is a JSON string. |

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

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| options | [SubscribeMessageOptions](arkts-arkui-featureability-subscribemessageoptions-i.md) | 是 | Options. |

## unsubscribeAbilityEvent

```TypeScript
static unsubscribeAbilityEvent(param: SubscribeAbilityEventParam): Promise<string>
```

Unsubscribe from events of an AA.

**起始版本：** 5

**ArkTS模式：** 仅支持ArkTS-Dyn，起始版本为5。

**废弃版本：** 8

<!--Device-FeatureAbility-static unsubscribeAbilityEvent(param: SubscribeAbilityEventParam): Promise<string>--><!--Device-FeatureAbility-static unsubscribeAbilityEvent(param: SubscribeAbilityEventParam): Promise<string>-End-->

**系统能力：** SystemCapability.ArkUI.ArkUI.Lite

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| param | [SubscribeAbilityEventParam](arkts-arkui-featureability-subscribeabilityeventparam-i.md) | 是 | Indicates the request param. |

**返回值：**

| 类型 | 说明 |
| --- | --- |
| Promise&lt;string&gt; | A Promise object is returned, which contains the result data returned by the AA. The result is a JSON string. |

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


# FeatureAbility

**Since:** 5

**Deprecated since:** 8

**Substitutes:** FeatureAbility

<!--Device-unnamed-export declare class FeatureAbility--><!--Device-unnamed-export declare class FeatureAbility-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

## callAbility

```TypeScript
static callAbility(param: CallAbilityParam): Promise<string>
```

Calls an AA.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static callAbility(param: CallAbilityParam): Promise<string>--><!--Device-FeatureAbility-static callAbility(param: CallAbilityParam): Promise<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [CallAbilityParam](arkts-arkui-featureability-callabilityparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## continueAbility

```TypeScript
static continueAbility(): Promise<Result>
```

Start FA migration.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static continueAbility(): Promise<Result>--><!--Device-FeatureAbility-static continueAbility(): Promise<Result>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Result](arkts-arkui-featureability-result-i.md)&gt; |

## finishWithResult

```TypeScript
static finishWithResult(param: FinishWithResultParams): Promise<Result>
```

FA call the interface to destroy itself and set the result as parameters.

**Since:** 5

**Deprecated since:** 8

**Substitutes:** terminateSelfWithResult

<!--Device-FeatureAbility-static finishWithResult(param: FinishWithResultParams): Promise<Result>--><!--Device-FeatureAbility-static finishWithResult(param: FinishWithResultParams): Promise<Result>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [FinishWithResultParams](arkts-arkui-featureability-finishwithresultparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Result](arkts-arkui-featureability-result-i.md)&gt; |

## getDeviceList

```TypeScript
static getDeviceList(flag: number): Promise<Result>
```

Get device information list.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static getDeviceList(flag: number): Promise<Result>--><!--Device-FeatureAbility-static getDeviceList(flag: number): Promise<Result>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| flag | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Result](arkts-arkui-featureability-result-i.md)&gt; |

## sendMsg

```TypeScript
static sendMsg(options: SendMessageOptions): void
```

Sends messages to the destination device.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static sendMsg(options: SendMessageOptions): void--><!--Device-FeatureAbility-static sendMsg(options: SendMessageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SendMessageOptions](arkts-arkui-featureability-sendmessageoptions-i.md) | Yes |

## startAbility

```TypeScript
static startAbility(request: RequestParams): Promise<Result>
```

Start a FA without callback result.

**Since:** 5

**Deprecated since:** 8

**Substitutes:** startAbility

<!--Device-FeatureAbility-static startAbility(request: RequestParams): Promise<Result>--><!--Device-FeatureAbility-static startAbility(request: RequestParams): Promise<Result>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [RequestParams](arkts-arkui-featureability-requestparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Result](arkts-arkui-featureability-result-i.md)&gt; |

## startAbilityForResult

```TypeScript
static startAbilityForResult(request: RequestParams): Promise<Result>
```

Start a FA with callback result.

**Since:** 5

**Deprecated since:** 8

**Substitutes:** startAbilityForResult

<!--Device-FeatureAbility-static startAbilityForResult(request: RequestParams): Promise<Result>--><!--Device-FeatureAbility-static startAbilityForResult(request: RequestParams): Promise<Result>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| request | [RequestParams](arkts-arkui-featureability-requestparams-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[Result](arkts-arkui-featureability-result-i.md)&gt; |

## subscribeAbilityEvent

```TypeScript
static subscribeAbilityEvent(param: SubscribeAbilityEventParam, func: Function): Promise<string>
```

Subscribe to events of an AA.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static subscribeAbilityEvent(param: SubscribeAbilityEventParam, func: Function): Promise<string>--><!--Device-FeatureAbility-static subscribeAbilityEvent(param: SubscribeAbilityEventParam, func: Function): Promise<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [SubscribeAbilityEventParam](arkts-arkui-featureability-subscribeabilityeventparam-i.md) | Yes |
| func | Function | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## subscribeMsg

```TypeScript
static subscribeMsg(options: SubscribeMessageOptions): void
```

Listens for messages sent from other devices.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static subscribeMsg(options: SubscribeMessageOptions): void--><!--Device-FeatureAbility-static subscribeMsg(options: SubscribeMessageOptions): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [SubscribeMessageOptions](arkts-arkui-featureability-subscribemessageoptions-i.md) | Yes |

## unsubscribeAbilityEvent

```TypeScript
static unsubscribeAbilityEvent(param: SubscribeAbilityEventParam): Promise<string>
```

Unsubscribe from events of an AA.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static unsubscribeAbilityEvent(param: SubscribeAbilityEventParam): Promise<string>--><!--Device-FeatureAbility-static unsubscribeAbilityEvent(param: SubscribeAbilityEventParam): Promise<string>-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| param | [SubscribeAbilityEventParam](arkts-arkui-featureability-subscribeabilityeventparam-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;string & gt; |

## unsubscribeMsg

```TypeScript
static unsubscribeMsg(): void
```

Cancel the listening for messages sent from other devices.

**Since:** 5

**Deprecated since:** 8

<!--Device-FeatureAbility-static unsubscribeMsg(): void--><!--Device-FeatureAbility-static unsubscribeMsg(): void-End-->

**System capability:** SystemCapability.ArkUI.ArkUI.Lite

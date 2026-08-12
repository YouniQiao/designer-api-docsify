# LiveFormExtensionContext

**LiveFormExtensionContext**, inherited from   
[ExtensionContext](./application/ExtensionContext:ExtensionContext), is the context of   
[LiveFormExtensionAbility](arkts-form-app-form-liveformextensionability-liveformextensionability-c.md#LiveFormExtensionAbility).

**Inheritance/Implementation:** LiveFormExtensionContext extends [ExtensionContext](ExtensionContext)

**Since:** 20

<!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext--><!--Device-unnamed-declare class LiveFormExtensionContext extends ExtensionContext-End-->

**System capability:** SystemCapability.Ability.Form

## connectServiceExtensionAbility

```TypeScript
public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): number
```

Connect a service extension ability.The destination of the connection must be a service extension.You must implement the [ConnectOptions](ConnectOptions) interface to obtain the proxy of the target service extension when the Service extension is connected.

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveFormExtensionContext-public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long--><!--Device-LiveFormExtensionContext-public connectServiceExtensionAbility(want: Want, connection: ConnectOptions): long-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| want | [Want](../../apis-ability-kit/arkts-apis/arkts-ability-app-ability-want-want-c.md) | Yes |
| connection | [ConnectOptions](../../apis-ability-kit/arkts-apis/arkts-ability-connectoptions-connectoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| number |

**Error codes:**

| Error Code ID |
| --- |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16501011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501011-api-not-supported) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |
| [16500100](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16500100-failed-to-obtain-widget-configuration-information) |

## disconnectServiceExtensionAbility

```TypeScript
public disconnectServiceExtensionAbility(connectionId: number): Promise<void>
```

Disconnect an ability to a service extension, in contrast to [connectServiceExtensionAbility](#connectServiceExtensionAbility).

**Since:** 21

**Model restriction:** This API can be used only in the stage model.

<!--Device-LiveFormExtensionContext-public disconnectServiceExtensionAbility(connectionId: long): Promise<void>--><!--Device-LiveFormExtensionContext-public disconnectServiceExtensionAbility(connectionId: long): Promise<void>-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| connectionId | number | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise & lt;void & gt; |

**Error codes:**

| Error Code ID |
| --- |
| [16501000](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501000-internal-function-error) |
| [16501011](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-form-kit/errorcode-form.md#16501011-api-not-supported) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

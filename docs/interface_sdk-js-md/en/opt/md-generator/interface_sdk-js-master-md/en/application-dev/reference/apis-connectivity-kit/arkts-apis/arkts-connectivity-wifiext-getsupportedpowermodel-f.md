# getSupportedPowerModel

## Modules to Import

```TypeScript
```

## getSupportedPowerModel

```TypeScript
function getSupportedPowerModel(): Promise<Array<PowerModel>>
```

Obtains the supported power model.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSupportedPowerMode](arkts-connectivity-wifimanagerext-getsupportedpowermode-f.md#getsupportedpowermode)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiext-function getSupportedPowerModel(): Promise<Array<PowerModel>>--><!--Device-wifiext-function getSupportedPowerModel(): Promise<Array<PowerModel>>-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;Array&lt;[PowerModel](arkts-connectivity-wifiext-powermodel-e.md)&gt;&gt; |


## getSupportedPowerModel

```TypeScript
function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void
```

Obtains the supported power model.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getSupportedPowerMode](arkts-connectivity-wifimanagerext-getsupportedpowermode-f.md#getsupportedpowermode)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiext-function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void--><!--Device-wifiext-function getSupportedPowerModel(callback: AsyncCallback<Array<PowerModel>>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;Array&lt;[PowerModel](arkts-connectivity-wifiext-powermodel-e.md)&gt;&gt; | Yes |

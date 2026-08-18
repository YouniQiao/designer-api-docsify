# getPowerModel

## Modules to Import

```TypeScript
```

## getPowerModel

```TypeScript
function getPowerModel(): Promise<PowerModel>
```

Obtains the current Wi-Fi power mode.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getPowerMode](arkts-connectivity-wifimanagerext-getpowermode-f.md#getpowermode)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiext-function getPowerModel(): Promise<PowerModel>--><!--Device-wifiext-function getPowerModel(): Promise<PowerModel>-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PowerModel](arkts-connectivity-wifiext-powermodel-e.md)&gt; |


## getPowerModel

```TypeScript
function getPowerModel(callback: AsyncCallback<PowerModel>): void
```

Obtains the current Wi-Fi power mode.

**Since:** 8

**Deprecated since:** 9

**Substitutes:** [getPowerMode](arkts-connectivity-wifimanagerext-getpowermode-f.md#getpowermode)

**Required permissions:** ohos.permission.GET_WIFI_INFO

<!--Device-wifiext-function getPowerModel(callback: AsyncCallback<PowerModel>): void--><!--Device-wifiext-function getPowerModel(callback: AsyncCallback<PowerModel>): void-End-->

**System capability:** SystemCapability.Communication.WiFi.AP.Extension

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| callback | [AsyncCallback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-asynccallback-i.md)&lt;[PowerModel](arkts-connectivity-wifiext-powermodel-e.md)&gt; | Yes |

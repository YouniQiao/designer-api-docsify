# unregCustomEapHandler

## Modules to Import

```TypeScript
import { eap } from 'kits/@kit.NetworkKit';
```

## unregCustomEapHandler

```TypeScript
function unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void
```

unreg the callback of eap packet customization.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 20; ArkTS-Sta since version 23.

**Required permissions:** ohos.permission.MANAGE_ENTERPRISE_WIFI_CONNECTION

<!--Device-eap-function unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void--><!--Device-eap-function unregCustomEapHandler(netType:number, eapCode: number, eapType: number, callback: Callback<EapData>): void-End-->

**System capability:** SystemCapability.Communication.NetManager.Eap

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| netType | number | Yes | Indicates net type need to customize. |
| eapCode | number | Yes | Indicates eap code need to customize. |
| eapType | number | Yes | Indicates eap type need to customize. |
| callback | [Callback](../../apis-basic-service-kit/arkts-apis/arkts-basicservices-base-callback-i.md)&lt;EapData&gt; | Yes | the callback of eap packet customization. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| 33200008 | Invalid eap type |
| 33200009 | netmanager stop |
| 201 | Permission denied. |
| 33200099 | internal error |
| 33200006 | Invalid net type |
| 33200007 | Invalid eap code |

## Examples

```TypeScript
import {eap} from '@kit.NetworkKit';
let netType = 1;
let eapCode = 1;
let eapType = 25;
let eapData = (eapData:eap.EapData):void => {
  console.info("rsp result", JSON.stringify(eapData));
};
    
eap.unregCustomEapHandler(netType, eapCode, eapType, eapData);
console.info('unregCustomEapHandler success');
```


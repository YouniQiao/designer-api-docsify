# removeAppShareOptions

## removeAppShareOptions

```TypeScript
function removeAppShareOptions(intention: Intention): void
```

Removes the data control information set by [setAppShareOptions]\_\_\_JSDOC\_LINK\_DESC\_USD\_0\_\_\_.

**Since:** 14

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

**Required permissions:** 
- API version 14+: ohos.permission.MANAGE_UDMF_APP_SHARE_OPTION

**Model restriction:** This API can be used only in the stage model.

<!--Device-unifiedDataChannel-function removeAppShareOptions(intention: Intention): void--><!--Device-unifiedDataChannel-function removeAppShareOptions(intention: Intention): void-End-->

**System capability:** SystemCapability.DistributedDataManager.UDMF.Core

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| intention | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | Type of the data channel. Currently, only the data channel of the **DRAG** type is supported. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes: 1. Mandatory parameters are left unspecified; 2. Incorrect parameter types; 3. Parameter verification failed. |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. Interface caller does not have permission " ohos.permission.MANAGE\_\_\_ESCAPED\_UNDERSCORE\_\_\_UDMF\_\_\_ESCAPED\_UNDERSCORE\_\_\_APP\_\_\_ESCAPED\_UNDERSCORE\_\_\_SHARE\_\_\_ESCAPED\_UNDERSCORE\_\_\_OPTION".\_\_\_HTML\_TAG\_USD\_0\_\_\_**Applicable version:** 14 and later |

**Example**

```TypeScript
import { BusinessError } from '@kit.BasicServicesKit';
try {
  unifiedDataChannel.removeAppShareOptions(unifiedDataChannel.Intention.DRAG);
  console.info(`[UDMF]removeAppShareOptions success. `);
}catch (e){
  let error: BusinessError = e as BusinessError;
  console.error(`[UDMF]removeAppShareOptions throws an exception. code is ${error.code}, message is ${error.message} `);
}
```


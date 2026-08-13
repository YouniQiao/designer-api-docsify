# wrapKeyItem

## Modules to Import

```TypeScript
import { huks } from '@kit.UniversalKeystoreKit';
```

## wrapKeyItem

```TypeScript
function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>
```

Wraps a key. This API uses a promise to return the result. > **NOTE：**> > Wrapping SE security level keys that defined in [HuksKeySecurityLevel](arkts-universalkeystore-huks-hukskeysecuritylevel-e.md#HuksKeySecurityLevel) > requires the ohos.permission.ACCESS_SE_KEY permission. &lt;!--Del--&gt;This feature is not supported currently.&lt;!--DelEnd--&gt;

**Since:** 20

**Deprecated since:** -1

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-huks-function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>--><!--Device-huks-function wrapKeyItem(keyAlias: string, params: HuksOptions): Promise<HuksReturnResult>-End-->

**System capability:** SystemCapability.Security.Huks.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| keyAlias | string | Yes |
| params | [HuksOptions](arkts-universalkeystore-huks-huksoptions-i.md) | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[HuksReturnResult](arkts-universalkeystore-huks-huksreturnresult-i.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [12000005](../errorcode-huks.md#12000005-ipc-error) |
| [12000004](../errorcode-huks.md#12000004-file-error) |
| [12000018](../errorcode-huks.md#12000018-invalid-input-parameter) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [12000014](../errorcode-huks.md#12000014-insufficient-memory) |
| [12000012](../errorcode-huks.md#12000012-external-error) |
| [12000011](../errorcode-huks.md#12000011-the-entity-does-not-exist) |
| [12000026](../errorcode-huks.md#12000026-secure-element-fault) |

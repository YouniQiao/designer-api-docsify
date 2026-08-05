# offReaderMode

## offReaderMode

```TypeScript
function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void
```

Disable foreground reader mode settings explicitly.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Required permissions:** ohos.permission.NFC_TAG

<!--Device-tag-function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void--><!--Device-tag-function offReaderMode(elementName: ElementName, callback?: AsyncCallback<TagInfo>): void-End-->

**System capability:** SystemCapability.Communication.NFC.Tag

**Parameters:**

| Name | Type | Mandatory | Description |
| --- | --- | --- | --- |
| elementName | \_\_\_MD\_LINK\_USD\_0\_\_\_ | Yes | The element name of application, must include the bundleName and abilityName. |
| callback | \_\_\_MD\_LINK\_USD\_0\_\_\_&lt;TagInfo&gt; | No | The callback to dispatched the TagInfo object for application. |

**Error codes:**

| Error Code ID | Error Message |
| --- | --- |
| [201](../../errorcode-universal.md#201-permission-denied) | Permission denied. |
| [401](../../apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) | Parameter error. Possible causes:1. Mandatory parameters are left unspecified.2. Incorrect parameter types.3. Parameter verification failed. |
| [801](../../apis-ads-kit/errorcode-ads.md#801-ad-request-failure) | Capability not supported. |
| [3100201](../errorcode-nfc.md#3100201-tag-readwrite-error) | The tag running state is abnormal in the service. |
| [3100203](../errorcode-nfc.md#3100203-incorrect-api-call-sequence) | The off() API can be called only when the on() has been called. |


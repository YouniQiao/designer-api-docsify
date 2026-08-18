# getPageContent (System API)

## Modules to Import

```TypeScript
```

## getPageContent

```TypeScript
function getPageContent(options?: ContentOptions): Promise<PageContent>
```

Obtains the onscreen content when a window is displayed on the screen.

**Since:** 23

**Required permissions:** ohos.permission.GET_SCREEN_CONTENT

<!--Device-onScreen-function getPageContent(options?: ContentOptions): Promise<PageContent>--><!--Device-onScreen-function getPageContent(options?: ContentOptions): Promise<PageContent>-End-->

**System capability:** SystemCapability.MultimodalAwareness.OnScreenAwareness

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| options | [ContentOptions](arkts-multimodalawareness-onscreen-contentoptions-i-sys.md) | No |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| Promise&lt;[PageContent](arkts-multimodalawareness-onscreen-pagecontent-i-sys.md)&gt; |

**Error codes:**

| Error Code ID |
| --- |
| [34000006](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000006-request-timeout) |
| [801](../../errorcode-universal.md#801-api-not-supported) |
| [34000004](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000004-page-not-ready) |
| [34000002](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000002-unsupported-application-or-page) |
| [34000003](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000003-invalid-window-id) |
| [34000001](../../apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) |
| [201](../../errorcode-universal.md#201-permission-denied) |
| [202](../../errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

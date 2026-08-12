# getPageContent (System API)

## Modules to Import

```TypeScript
import { onScreen } from '@kit.MultimodalAwarenessKit';
```

## getPageContent

```TypeScript
function getPageContent(options?: ContentOptions): Promise<PageContent>
```

Obtains the onscreen content when a window is displayed on the screen.

**Since:** 20

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
| [34000006](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-onScreen.md#34000006-request-timeout) |
| [801](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#801-ad-request-failure) |
| [34000004](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-onScreen.md#34000004-page-not-ready) |
| [34000002](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-onScreen.md#34000002-unsupported-application-or-page) |
| [34000003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-onScreen.md#34000003-invalid-window-id) |
| [34000001](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-multimodalawareness-kit/errorcode-onScreen.md#34000001-service-exception) |
| [201](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#201-permission-denied) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

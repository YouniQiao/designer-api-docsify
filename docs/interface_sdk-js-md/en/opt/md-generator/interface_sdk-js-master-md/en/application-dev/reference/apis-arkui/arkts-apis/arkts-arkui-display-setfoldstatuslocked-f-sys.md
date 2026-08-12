# setFoldStatusLocked (System API)

## Modules to Import

```TypeScript
import { display } from '@kit.ArkUI';
```

## setFoldStatusLocked

```TypeScript
function setFoldStatusLocked(locked: boolean): void
```

Sets whether to lock the current fold status of the foldable device.

**Since:** 11

<!--Device-display-function setFoldStatusLocked(locked: boolean): void--><!--Device-display-function setFoldStatusLocked(locked: boolean): void-End-->

**System capability:** SystemCapability.Window.SessionManager

**System API:** This is a system API.

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| locked | boolean | Yes |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-ads-kit/errorcode-ads.md#401-incorrect-ads-request-parameter) |
| [1400003](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/apis-arkui/errorcode-display.md#1400003-abnormal-display-manager-service) |
| [202](../../../../../../../../gitee_tmp/docs/master/en/application-dev/reference/errorcode-universal.md#202-permission-verification-failed-for-calling-a-system-api) |

## Examples

```TypeScript
import { display } from '@kit.ArkUI';

try {
  let locked: boolean = false;
  // Set the fold status to not locked.
  display.setFoldStatusLocked(locked);
} catch (exception) {
  console.error(`Failed to change the fold status locked mode. Code: ${exception.code}, message: ${exception.message}`);
}
```

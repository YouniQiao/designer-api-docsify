# findWindow

## Modules to Import

```TypeScript
```

## findWindow

```TypeScript
function findWindow(name: string): Window
```

Finds a window based on the name.

**Since:** 23

**Atomic service API:** This API can be used in atomic services since API version 11.

<!--Device-window-function findWindow(name: string): Window--><!--Device-window-function findWindow(name: string): Window-End-->

**System capability:** SystemCapability.WindowManager.WindowManager.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| name | string | Yes |

**Return value:**

| [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) |
| --- |
| [Window](arkts-arkui-window-window-i.md) |

**Error codes:**

| Error Code ID |
| --- |
| [401](../../errorcode-universal.md#401-parameter-check-failed) |
| [1300002](../errorcode-window.md#1300002-abnormal-window-state) |

**Examples**

```TypeScript
let windowClass: window.Window | undefined = undefined;
try {
  windowClass = window.findWindow('test');
} catch (exception) {
  console.error(`Failed to find the Window. Cause code: ${exception.code}, message: ${exception.message}`);
}
```

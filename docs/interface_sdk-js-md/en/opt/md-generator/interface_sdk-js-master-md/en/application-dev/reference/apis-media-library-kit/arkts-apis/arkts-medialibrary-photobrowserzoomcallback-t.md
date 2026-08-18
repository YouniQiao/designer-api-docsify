# PhotoBrowserZoomCallback

```TypeScript
export type PhotoBrowserZoomCallback = (scale: number) => void
```

Callback to be invoked when the large image is zoomed in or out after the large image is entered through the **PhotoPickerComponent**.

**Since:** 26.0.0

**Model restriction:** This API can be used only in the stage model.

**Atomic service API:** This API can be used in atomic services since API version 26.0.0.

<!--Device-unnamed-export type PhotoBrowserZoomCallback = (scale: double) => void--><!--Device-unnamed-export type PhotoBrowserZoomCallback = (scale: double) => void-End-->

**System capability:** SystemCapability.FileManagement.PhotoAccessHelper.Core

**Parameters:**

| [Name](../../apis-contacts-kit/arkts-apis/arkts-contacts-contact-name-c.md) | [Type](../../apis-arkts/arkts-apis/arkts-arkts-util-type-e.md) | Mandatory |
| --- | --- | --- |
| scale | number | Yes |

# BlanklessLoadingParam

Defines the blankless loading parameter. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

<!--Device-webview-interface BlanklessLoadingParam--><!--Device-webview-interface BlanklessLoadingParam-End-->

**System capability:** SystemCapability.Web.Webview.Core

## callback

```TypeScript
callback?: Callback<BlanklessFrameInterpolationInfo>
```

Callback for the blankless frame interpolation, which is used to return the blankless frame interpolation information. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Type:** Callback&lt;BlanklessFrameInterpolationInfo&gt;

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessLoadingParam-callback?: Callback<BlanklessFrameInterpolationInfo>--><!--Device-BlanklessLoadingParam-callback?: Callback<BlanklessFrameInterpolationInfo>-End-->

**System capability:** SystemCapability.Web.Webview.Core

## duration

```TypeScript
duration?: int
```

Duration of the frame interpolation. The valid range is the union of {0} and [200, 2000]. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned. The value must be an integer. \_\_\_HTML\_TAG\_DESC\_USD\_0\_\_\_Unit: ms.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessLoadingParam-duration?: int--><!--Device-BlanklessLoadingParam-duration?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core

## enable

```TypeScript
enable: boolean
```

Whether to enable frame interpolation. The value true indicates to enable frame interpolation, and false indicates the opposite. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Type:** boolean

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessLoadingParam-enable: boolean--><!--Device-BlanklessLoadingParam-enable: boolean-End-->

**System capability:** SystemCapability.Web.Webview.Core

## expirationTime

```TypeScript
expirationTime?: int
```

Expiration time of the historical frame, in ms (UTC time). T indicates the current UTC time. If the expiration time is 30 days, the value is 2592000000 ms. The value range is the union of (T, T + 2592000000] and {0}. 0 indicates that the expiration time is not specified and the default expiration time (7 days) is used. Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Type:** int

**Since:** 23

**ArkTS mode:** ArkTS-Sta only, since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BlanklessLoadingParam-expirationTime?: int--><!--Device-BlanklessLoadingParam-expirationTime?: int-End-->

**System capability:** SystemCapability.Web.Webview.Core


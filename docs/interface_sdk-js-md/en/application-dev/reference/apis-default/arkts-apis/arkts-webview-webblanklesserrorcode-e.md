# WebBlanklessErrorCode

Enumerates the error codes of blankless. For details, see [setBlanklessLoadingWithKey](arkts-webview-webviewcontroller-c.md#setblanklessloadingwithkey) or [BlanklessInfo](arkts-webview-blanklessinfo-i.md).

@enum { number }

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-webview-enum WebBlanklessErrorCode--><!--Device-webview-enum WebBlanklessErrorCode-End-->

**System capability:** SystemCapability.Web.Webview.Core

## SUCCESS

```TypeScript
SUCCESS = 0
```

The operation is successful.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebBlanklessErrorCode-SUCCESS = 0--><!--Device-WebBlanklessErrorCode-SUCCESS = 0-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_UNKNOWN

```TypeScript
ERR_UNKNOWN = -1
```

Unknown error.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebBlanklessErrorCode-ERR_UNKNOWN = -1--><!--Device-WebBlanklessErrorCode-ERR_UNKNOWN = -1-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_INVALID_PARAM

```TypeScript
ERR_INVALID_PARAM = -2
```

Invalid parameter.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebBlanklessErrorCode-ERR_INVALID_PARAM = -2--><!--Device-WebBlanklessErrorCode-ERR_INVALID_PARAM = -2-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_CONTROLLER_NOT_INITED

```TypeScript
ERR_CONTROLLER_NOT_INITED = -3
```

The web controller is not bound to any component.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebBlanklessErrorCode-ERR_CONTROLLER_NOT_INITED = -3--><!--Device-WebBlanklessErrorCode-ERR_CONTROLLER_NOT_INITED = -3-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_KEY_NOT_MATCH

```TypeScript
ERR_KEY_NOT_MATCH = -4
```

The key value is not matched. This error code is returned when the key values of setBlanklessLodingWithKey and getBlanklessInfoWithKey are not matched.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebBlanklessErrorCode-ERR_KEY_NOT_MATCH = -4--><!--Device-WebBlanklessErrorCode-ERR_KEY_NOT_MATCH = -4-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_SIGNIFICANT_CHANGE

```TypeScript
ERR_SIGNIFICANT_CHANGE = -5
```

The system determines that the change is too large when the similarity is less than 0.33. As a result, the setBlanklessLodingWithKey API fails to enable frame interpolation.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

<!--Device-WebBlanklessErrorCode-ERR_SIGNIFICANT_CHANGE = -5--><!--Device-WebBlanklessErrorCode-ERR_SIGNIFICANT_CHANGE = -5-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_DURATION_OUT_OF_RANGE

```TypeScript
ERR_DURATION_OUT_OF_RANGE = -6
```

The value of BlanklessLoadingParam.duration is out of the valid value range.

Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebBlanklessErrorCode-ERR_DURATION_OUT_OF_RANGE = -6--><!--Device-WebBlanklessErrorCode-ERR_DURATION_OUT_OF_RANGE = -6-End-->

**System capability:** SystemCapability.Web.Webview.Core

## ERR_EXPIRATION_TIME_OUT_OF_RANGE

```TypeScript
ERR_EXPIRATION_TIME_OUT_OF_RANGE = -7
```

The value of BlanklessLoadingParam.expirationTime is invalid.

Device behavior differences: Only the mobile phone is supported. For other devices, 801 is returned.

**Since:** 23

**ArkTS mode:** ArkTS-Sta since version 23.

**Model restriction:** This API can be used only in the stage model.

<!--Device-WebBlanklessErrorCode-ERR_EXPIRATION_TIME_OUT_OF_RANGE = -7--><!--Device-WebBlanklessErrorCode-ERR_EXPIRATION_TIME_OUT_OF_RANGE = -7-End-->

**System capability:** SystemCapability.Web.Webview.Core


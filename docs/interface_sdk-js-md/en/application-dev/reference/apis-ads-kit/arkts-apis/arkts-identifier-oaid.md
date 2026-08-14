# @ohos.identifier.oaid

This module provides the capability of obtaining and resetting the Open Anonymous Device Identifier (OAID). > **NOTE：**> To use the API for obtaining the OAID, you need to > [request user authorization](../../../security/AccessToken/request-user-authorization.md) (the permission is > enabled by default): ohos.permission.APP_TRACKING_CONSENT.

**Since:** 10

**ArkTS mode:** ArkTS-Dyn only, since version 10.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace identifier--><!--Device-unnamed-declare namespace identifier-End-->

**System capability:** SystemCapability.Advertising.OAID

## Modules to Import

```TypeScript
import { identifier } from 'identifier';
```

## Summary

### Functions

| Name | Description |
| --- | --- |
| [getOAID](arkts-ads-identifier-getoaid-f.md#getOAID) | Obtains the OAID. This API uses an asynchronous callback to return the result. > **NOTE：**> > The setting item of cross-app association access permission was named app tracking access permission > in HarmonyOS NEXT Developer Beta5 and earlier versions. |
| [getOAID](arkts-ads-identifier-getoaid-f.md#getOAID) | Obtains the OAID. This API uses a promise to return the result. > **NOTE：**> > The setting item of cross-app association access permission was named app tracking access permission > in HarmonyOS NEXT Developer Beta5 and earlier versions. |

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [resetOAID](arkts-ads-identifier-resetoaid-f-sys.md#resetOAID) | Resets the OAID. |
<!--DelEnd-->


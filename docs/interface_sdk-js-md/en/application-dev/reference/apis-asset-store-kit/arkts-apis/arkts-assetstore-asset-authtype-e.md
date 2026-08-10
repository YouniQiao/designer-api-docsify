# AuthType

枚举，关键资产支持的用户认证类型。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

<!--Device-asset-enum AuthType--><!--Device-asset-enum AuthType-End-->

**System capability:** SystemCapability.Security.Asset

## NONE

```TypeScript
NONE = 0x00
```

访问关键资产前无需用户认证。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AuthType-NONE = 0x00--><!--Device-AuthType-NONE = 0x00-End-->

**System capability:** SystemCapability.Security.Asset

## ANY

```TypeScript
ANY = 0xFF
```

任意一种用户认证方式（PIN码、人脸、指纹等）通过后，均可访问关键资产。

**Since:** 11

**ArkTS mode:** ArkTS-Dyn only, since version 11.

**Atomic service API:** This API can be used in atomic services since API version 14.

<!--Device-AuthType-ANY = 0xFF--><!--Device-AuthType-ANY = 0xFF-End-->

**System capability:** SystemCapability.Security.Asset


# GrantedBundleInfo

描述已授权的包信息。

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-unnamed-export interface GrantedBundleInfo--><!--Device-unnamed-export interface GrantedBundleInfo-End-->

**系统能力：** SystemCapability.Notification.Notification

## appIndex

```TypeScript
readonly appIndex: int
```

应用的分身索引标识，仅在分身应用中生效。从[ApplicationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-applicationinfo-i.md/arkts-ability-applicationinfo-i.md)中appIndex获取。

**类型：** ArkTS-Dyn: number  <br>ArkTS-Sta：int

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-GrantedBundleInfo-readonly appIndex: int--><!--Device-GrantedBundleInfo-readonly appIndex: int-End-->

**系统能力：** SystemCapability.Notification.Notification

## appName

```TypeScript
readonly appName?: string
```

应用的名称。从[ApplicationInfo](../../apis-ability-kit/arkts-apis/arkts-ability-applicationinfo-i.md/arkts-ability-applicationinfo-i.md)中label获取。

**类型：** string

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-GrantedBundleInfo-readonly appName?: string--><!--Device-GrantedBundleInfo-readonly appName?: string-End-->

**系统能力：** SystemCapability.Notification.Notification

## bundleName

```TypeScript
bundleName: string
```

应用的包名。

**类型：** string

**起始版本：** 22

**ArkTS模式：** ArkTS-Dyn起始版本为22；ArkTS-Sta起始版本为23。

<!--Device-GrantedBundleInfo-bundleName: string--><!--Device-GrantedBundleInfo-bundleName: string-End-->

**系统能力：** SystemCapability.Notification.Notification


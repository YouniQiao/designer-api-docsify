# UserGrantSetting

描述用户授权的设置信息。

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

<!--Device-unnamed-export interface UserGrantSetting--><!--Device-unnamed-export interface UserGrantSetting-End-->

**System capability:** SystemCapability.Notification.Notification

## grantedBundleInfos

```TypeScript
readonly grantedBundleInfos?: Array<GrantedBundleInfo>
```

“已获取的本机通知”通知开关开启的应用列表。

**Type:** Array&lt;GrantedBundleInfo&gt;

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserGrantSetting-readonly grantedBundleInfos?: Array<GrantedBundleInfo>--><!--Device-UserGrantSetting-readonly grantedBundleInfos?: Array<GrantedBundleInfo>-End-->

**System capability:** SystemCapability.Notification.Notification

## userGrantEnabled

```TypeScript
readonly userGrantEnabled: boolean
```

“允许获取本机通知”的开关状态。 true：表示功能已启用；false：表示功能未启用。

**Type:** boolean

**Since:** 26.0.0

**ArkTS mode:** Both ArkTS-Dyn and ArkTS-Sta, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-UserGrantSetting-readonly userGrantEnabled: boolean--><!--Device-UserGrantSetting-readonly userGrantEnabled: boolean-End-->

**System capability:** SystemCapability.Notification.Notification


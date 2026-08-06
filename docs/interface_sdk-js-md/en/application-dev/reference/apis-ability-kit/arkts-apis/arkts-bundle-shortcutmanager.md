# @ohos.bundle.shortcutManager

This module provides the application's management capabilities for shortcuts, including setting whether a shortcut is displayed. Through shortcuts, users can quickly launch specific features of an app from the home screen,improving the app's ease of use and user retention. Typical usage scenarios include: providing users with quick access to frequently used features, dynamically adjusting the display of shortcuts based on user habits, etc.

**Since:** 20

**ArkTS mode:** ArkTS-Dyn since version 12; ArkTS-Sta since version 23.

<!--Device-unnamed-declare namespace shortcutManager--><!--Device-unnamed-declare namespace shortcutManager-End-->

**System capability:** SystemCapability.BundleManager.BundleFramework.Launcher

## Summary

### Functions

| Name | Description |
| --- | --- |
| [addDesktopShortcutInfo](arkts-ability-shortcutmanager-adddesktopshortcutinfo-f.md#adddesktopshortcutinfo) | Adds a shortcut for the given user. This API uses a promise to return the result. |
| [addDynamicShortcutInfos](arkts-ability-shortcutmanager-adddynamicshortcutinfos-f.md#adddynamicshortcutinfos) | Adds dynamic shortcuts for the given user. |
| [deleteDesktopShortcutInfo](arkts-ability-shortcutmanager-deletedesktopshortcutinfo-f.md#deletedesktopshortcutinfo) | Deletes a shortcut for the given user. This API uses a promise to return the result. |
| [deleteDynamicShortcutInfos](arkts-ability-shortcutmanager-deletedynamicshortcutinfos-f.md#deletedynamicshortcutinfos) | Deletes dynamic shortcuts. |
| [getAllDesktopShortcutInfo](arkts-ability-shortcutmanager-getalldesktopshortcutinfo-f.md#getalldesktopshortcutinfo) | Obtains the information about all shortcuts of the given user. |
| [getAllShortcutInfoForSelf](arkts-ability-shortcutmanager-getallshortcutinfoforself-f.md#getallshortcutinfoforself) | Obtains all the shortcut information defined in the  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ file of the current application. This API uses a promise to return the result. |
| [getShortcutInfoByAbility](arkts-ability-shortcutmanager-getshortcutinfobyability-f.md#getshortcutinfobyability) | Obtains shortcut info by bundleName, moduleName, abilityName, userId and appIndex.If you need to obtains shortcut info under the current user, ohos.permission.GET\_\_\_ESCAPED\_UNDERSCORE\_\_\_BUNDLE\_\_\_ESCAPED\_UNDERSCORE\_\_\_INFO\_\_\_ESCAPED\_UNDERSCORE\_\_\_PRIVILEGED needs to be applied for.If you need to obtains shortcut info under other users, ohos.permission.GET\_\_\_ESCAPED\_UNDERSCORE\_\_\_BUNDLE\_\_\_ESCAPED\_UNDERSCORE\_\_\_INFO\_\_\_ESCAPED\_UNDERSCORE\_\_\_PRIVILEGED and ohos.permission.INTERACT\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACROSS\_\_\_ESCAPED\_UNDERSCORE\_\_\_LOCAL\_\_\_ESCAPED\_UNDERSCORE\_\_\_ACCOUNTS need to be applied for. |
| [isShortcutSupported](arkts-ability-shortcutmanager-isshortcutsupported-f.md#isshortcutsupported) | Checks whether the current device supports shortcuts. |
| [setShortcutVisibleForSelf](arkts-ability-shortcutmanager-setshortcutvisibleforself-f.md#setshortcutvisibleforself) | Sets whether to display the specified shortcut for the current application. This API uses a promise to return the result. |
| [setShortcutsEnabled](arkts-ability-shortcutmanager-setshortcutsenabled-f.md#setshortcutsenabled) | Enables or disables the specified static shortcuts. This API uses a promise to return the result. |
| [updateDesktopShortcutInfo](arkts-ability-shortcutmanager-updatedesktopshortcutinfo-f.md#updatedesktopshortcutinfo) | Updates a shortcut for the given user. This API uses a promise to return the result. |

### Types

| Name | Description |
| --- | --- |
| [ParameterItem](arkts-ability-shortcutmanager-parameteritem-t.md) | Defines the custom data in the shortcut configuration. |
| [ShortcutInfo](arkts-ability-shortcutmanager-shortcutinfo-t.md) | Defines the shortcut information defined in the  \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ file of the application. |
| [ShortcutWant](arkts-ability-shortcutmanager-shortcutwant-t.md) | Defines the target \_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_MD\_\_\_ESCAPED\_UNDERSCORE\_\_\_LINK\_\_\_ESCAPED\_UNDERSCORE\_\_\_DESC\_\_\_ESCAPED\_UNDERSCORE\_\_\_USD\_\_\_ESCAPED\_UNDERSCORE\_\_\_0\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_\_\_\_ESCAPED\_UNDERSCORE\_\_\_ defined in the shortcut configuration. |


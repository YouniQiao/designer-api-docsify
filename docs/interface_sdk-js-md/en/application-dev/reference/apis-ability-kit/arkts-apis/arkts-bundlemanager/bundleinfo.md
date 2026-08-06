# bundleManager/BundleInfo

The module defines the bundle information. An application can obtain its own bundle information through
 [bundleManager.getBundleInfoForSelf](../arkts-ability-bundlemanager-getbundleinfoforself-f.md#getbundleinfoforself)
 , with [bundleFlags](../arkts-ability-bundlemanager-bundleflag-e.md) set to the information to be
 contained in the returned [BundleInfo](../arkts-ability-bundlemanager/bundleinfo-bundleinfo-i.md).


## Summary

### Interfaces

| Name | Description |
| --- | --- |
| [AlternateIconInfo](bundleinfo-alternateiconinfo-i.md) | Describes the app backup icon information. |
| [AppCloneIdentity](bundleinfo-appcloneidentity-i.md) | Describes the identity information of an application clone. |
| [BundleInfo](bundleinfo-bundleinfo-i.md) | The module defines the bundle information. |
| [ReqPermissionDetail](bundleinfo-reqpermissiondetail-i.md) | Provides the detailed information of the permissions to request from the system. |
| [SignatureInfo](bundleinfo-signatureinfo-i.md) | Describes the signature information of the app package,which can identifythe app source, ensure app integrity,and be used for app security verification and identification. |
| [UsedScene](bundleinfo-usedscene-i.md) | Describes the use scenario and timing of the permission,helping developers request and use permissions properly. |

<!--Del-->
### Interfaces（系统接口）

| Name | Description |
| --- | --- |
| [AppClonePreference](bundleinfo-appclonepreference-i-sys.md) | Defines the application clone preference configuration. |
| [BundleInfo](bundleinfo-bundleinfo-i-sys.md) | The module defines the bundle information. |
| [BundleOptions](bundleinfo-bundleoptions-i-sys.md) | The bundle options of bundle manager |
| [DynamicIconInfo](bundleinfo-dynamiciconinfo-i-sys.md) | Obtains dynamic icon information about a bundle |
<!--DelEnd-->


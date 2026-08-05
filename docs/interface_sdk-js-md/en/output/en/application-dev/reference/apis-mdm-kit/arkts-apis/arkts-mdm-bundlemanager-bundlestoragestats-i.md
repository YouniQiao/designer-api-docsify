# BundleStorageStats

Storage usage information of the application.

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

<!--Device-bundleManager-interface BundleStorageStats--><!--Device-bundleManager-interface BundleStorageStats-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## appSize

```TypeScript
appSize: number
```

Size of the application installation files, in bytes. Application installation file directory: /data/storage/el1/bundle

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleStorageStats-appSize: number--><!--Device-BundleStorageStats-appSize: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## bundleName

```TypeScript
bundleName: string
```

Bundle name of the application.

**Type:** string

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleStorageStats-bundleName: string--><!--Device-BundleStorageStats-bundleName: string-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager

## dataSize

```TypeScript
dataSize: number
```

Size of the local data, distributed data, and database data of the application, in bytes. Local file directory (parent directory of the cache file directory): /data/storage/\${el1-el5}/base Distributed file directory: /data/storage/el2/distributedfiles Database file directory: /data/storage/\${el1-el5}/database **Note**: **\${el1-el5}** refers to the directories \_\_\_MD\_LINK\_DESC\_USD\_0\_\_\_

**Type:** number

**Since:** 26.0.0

**ArkTS mode:** ArkTS-Dyn only, since version 26.0.0.

**Model restriction:** This API can be used only in the stage model.

<!--Device-BundleStorageStats-dataSize: number--><!--Device-BundleStorageStats-dataSize: number-End-->

**System capability:** SystemCapability.Customization.EnterpriseDeviceManager


# @ohos.application.formHost

The **formHost** module provides APIs related to the widget host, which is an application that displays the widget content and controls the position where the widget is displayed. You can use the APIs to delete, release, and update widgets installed by the same user, and obtain widget information and status.

**Since:** 8

**ArkTS mode:** ArkTS-Dyn only, since version 8.

**Deprecated since:** 9

**Substitutes:** [formHost](arkts-app-form-formhost.md#@ohos.app.form.formHost)

<!--Device-unnamed-declare namespace formHost--><!--Device-unnamed-declare namespace formHost-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [acquireFormState](arkts-form-formhost-acquireformstate-depr-f-sys.md#acquireFormState) | Obtains the widget state. This API uses an asynchronous callback to return the result. |
| [acquireFormState](arkts-form-formhost-acquireformstate-depr-f-sys.md#acquireFormState) | Obtains the widget state. This API uses a promise to return the result. |
| [castTempForm](arkts-form-formhost-casttempform-depr-f-sys.md#castTempForm) | Converts a temporary widget to a normal one. This API uses an asynchronous callback to return the result. |
| [castTempForm](arkts-form-formhost-casttempform-depr-f-sys.md#castTempForm) | Converts a temporary widget to a normal one. This API uses a promise to return the result. |
| [deleteForm](arkts-form-formhost-deleteform-depr-f-sys.md#deleteForm) | Deletes a widget. After this API is called, the application can no longer use the widget, and the Widget Manager will not retain the widget information. This API uses an asynchronous callback to return the result. |
| [deleteForm](arkts-form-formhost-deleteform-depr-f-sys.md#deleteForm) | Deletes a widget. After this API is called, the application can no longer use the widget, and the Widget Manager will not retain the widget information. This API uses a promise to return the result. |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-depr-f-sys.md#deleteInvalidForms) | Deletes invalid widgets from the list. This API uses an asynchronous callback to return the result. |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-depr-f-sys.md#deleteInvalidForms) | Deletes invalid widgets from the list. This API uses a promise to return the result. |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-depr-f-sys.md#disableFormsUpdate) | Instructs the widget framework to make a widget not updatable. After this API is called, the widget cannot receive updates from the widget provider. This API uses an asynchronous callback to return the result. |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-depr-f-sys.md#disableFormsUpdate) | Instructs the widget framework to make a widget not updatable. After this API is called, the widget cannot receive updates from the widget provider. This API uses a promise to return the result. |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-depr-f-sys.md#enableFormsUpdate) | Instructs the widget framework to make a widget updatable. After this API is called, the widget is in the enabled state and can receive updates from the widget provider. This API uses an asynchronous callback to return the result. |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-depr-f-sys.md#enableFormsUpdate) | Instructs the widget framework to make a widget updatable. After this API is called, the widget is in the enabled state and can receive updates from the widget provider. This API uses a promise to return the result. |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-depr-f-sys.md#getAllFormsInfo) | Obtains the widget information provided by all applications on the device. This API uses an asynchronous callback to return the result. |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-depr-f-sys.md#getAllFormsInfo) | Obtains the widget information provided by all applications on the device. This API uses a promise to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-depr-f-sys.md#getFormsInfo) | Obtains the widget information provided by a given application on the device. This API uses an asynchronous callback to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-depr-f-sys.md#getFormsInfo) | Obtains the widget information provided by a given application on the device. This API uses an asynchronous callback to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-depr-f-sys.md#getFormsInfo) | Obtains the widget information provided by a given application on the device. This API uses a promise to return the result. |
| [isSystemReady](arkts-form-formhost-issystemready-depr-f-sys.md#isSystemReady) | Checks whether the system is ready. This API uses an asynchronous callback to return the result. |
| [isSystemReady](arkts-form-formhost-issystemready-depr-f-sys.md#isSystemReady) | Checks whether the system is ready. This API uses a promise to return the result. |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-depr-f-sys.md#notifyFormsEnableUpdate) | Instructs the widgets to enable or disable updates. This API uses an asynchronous callback to return the result. |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-depr-f-sys.md#notifyFormsEnableUpdate) | Instructs the widgets to enable or disable updates. This API uses a promise to return the result. |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-depr-f-sys.md#notifyFormsVisible) | Instructs the widgets to make themselves visible. This API uses an asynchronous callback to return the result. |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-depr-f-sys.md#notifyFormsVisible) | Instructs the widgets to make themselves visible. This API uses a promise to return the result. |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-depr-f-sys.md#notifyInvisibleForms) | Instructs the widget framework to make a widget invisible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses an asynchronous callback to return the result. |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-depr-f-sys.md#notifyInvisibleForms) | Instructs the widget framework to make a widget invisible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses a promise to return the result. |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-depr-f-sys.md#notifyVisibleForms) | Instructs the widget framework to make a widget visible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses an asynchronous callback to return the result. |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-depr-f-sys.md#notifyVisibleForms) | Instructs the widget framework to make a widget visible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses a promise to return the result. |
| [off_formUninstall](arkts-form-formhost-offformuninstall-depr-f-sys.md#off_formUninstall) | Unsubscribes from widget uninstall events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget > is automatically uninstalled. |
| [on_formUninstall](arkts-form-formhost-onformuninstall-depr-f-sys.md#on_formUninstall) | Subscribes to widget uninstall events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget > is automatically uninstalled. |
| [releaseForm](arkts-form-formhost-releaseform-depr-f-sys.md#releaseForm) | Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager still retains the widget cache and storage information. This API uses an asynchronous callback to return the result. |
| [releaseForm](arkts-form-formhost-releaseform-depr-f-sys.md#releaseForm) | Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager retains the storage information about the widget and retains or releases the cache information based on the setting. This API uses an asynchronous callback to return the result. |
| [releaseForm](arkts-form-formhost-releaseform-depr-f-sys.md#releaseForm) | Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager retains the storage information about the widget and retains or releases the cache information based on the setting. This API uses a promise to return the result. |
| [requestForm](arkts-form-formhost-requestform-depr-f-sys.md#requestForm) | Requests a widget update. This API uses an asynchronous callback to return the result. |
| [requestForm](arkts-form-formhost-requestform-depr-f-sys.md#requestForm) | Requests a widget update. This API uses a promise to return the result. |
<!--DelEnd-->


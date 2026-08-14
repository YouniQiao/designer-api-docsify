# @ohos.app.form.formHost

The **formHost** module provides APIs related to the widget host, which is an application that displays the widget content and controls the position where the widget is displayed. You can use the APIs to delete, release, and update widgets installed by the same user, and obtain widget information and status.

**Since:** 23

**ArkTS mode:** ArkTS-Dyn only, since version 23.

**Deprecated since:** -1

<!--Device-unnamed-declare namespace formHost--><!--Device-unnamed-declare namespace formHost-End-->

**System capability:** SystemCapability.Ability.Form

**System API:** This is a system API.

## Modules to Import

```TypeScript
import { formHost } from 'formHost';
```

## Summary

<!--Del-->
### Functions（系统接口）

| Name | Description |
| --- | --- |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireFormData) | Requests data from the widget provider. This API uses an asynchronous callback to return the result. |
| [acquireFormData](arkts-form-formhost-acquireformdata-f-sys.md#acquireFormData-(System-API)) | Requests data from the widget provider. This API uses a promise to return the result. |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireFormState) | Obtains the widget state. This API uses an asynchronous callback to return the result. |
| [acquireFormState](arkts-form-formhost-acquireformstate-f-sys.md#acquireFormState-(System-API)) | Obtains the widget state. This API uses a promise to return the result. |
| [addForm](arkts-form-formhost-addform-f-sys.md#addForm) | Add a form. You can use this method to create a theme form. |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#castToNormalForm) | Converts a temporary widget to a normal one. This API uses an asynchronous callback to return the result. |
| [castToNormalForm](arkts-form-formhost-casttonormalform-f-sys.md#castToNormalForm-(System-API)) | Converts a temporary widget to a normal one. This API uses a promise to return the result. |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearRouterProxy) | Clears the router proxy set for widgets. This API uses an asynchronous callback to return the result. |
| [clearRouterProxy](arkts-form-formhost-clearrouterproxy-f-sys.md#clearRouterProxy-(System-API)) | Clears the router proxy set for widgets. This API uses a promise to return the result. |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteForm) | Deletes a widget. After this API is called, the application can no longer use the widget, and the Widget Manager will not retain the widget information. This API uses an asynchronous callback to return the result. |
| [deleteForm](arkts-form-formhost-deleteform-f-sys.md#deleteForm-(System-API)) | Deletes a widget. After this API is called, the application can no longer use the widget, and the Widget Manager will not retain the widget information. This API uses a promise to return the result. |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteInvalidForms) | Deletes invalid widgets from the list. This API uses an asynchronous callback to return the result. |
| [deleteInvalidForms](arkts-form-formhost-deleteinvalidforms-f-sys.md#deleteInvalidForms-(System-API)) | Deletes invalid widgets from the list. This API uses a promise to return the result. |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableFormsUpdate) | Instructs the widget framework to make a widget not updatable. After this API is called, the widget cannot receive updates from the widget provider. This API uses an asynchronous callback to return the result. |
| [disableFormsUpdate](arkts-form-formhost-disableformsupdate-f-sys.md#disableFormsUpdate-(System-API)) | Instructs the widget framework to make a widget not updatable. After this API is called, the widget cannot receive updates from the widget provider. This API uses a promise to return the result. |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableFormsUpdate) | Instructs the widget framework to make a widget updatable. After this API is called, the widget is in the enabled state and can receive updates from the widget provider. This API uses an asynchronous callback to return the result. |
| [enableFormsUpdate](arkts-form-formhost-enableformsupdate-f-sys.md#enableFormsUpdate-(System-API)) | Instructs the widget framework to make a widget updatable. After this API is called, the widget is in the enabled state and can receive updates from the widget provider. This API uses a promise to return the result. |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getAllFormsInfo) | Obtains the widget information provided by all applications on the device (excluding template widgets). This API uses an asynchronous callback to return the result. |
| [getAllFormsInfo](arkts-form-formhost-getallformsinfo-f-sys.md#getAllFormsInfo-(System-API)) | Obtains the widget information provided by all applications on the device (excluding template widgets). This API uses a promise to return the result. |
| [getAllTemplateFormsInfo](arkts-form-formhost-getalltemplateformsinfo-f-sys.md#getAllTemplateFormsInfo) | Obtains the template widget information provided by all applications on the device. This API uses a promise to return the result. |
| [getFormIdsByFormLocation](arkts-form-formhost-getformidsbyformlocation-f-sys.md#getFormIdsByFormLocation) | Obtains the list of widget IDs at a specified location on the device. This API uses a promise to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo) | Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses an asynchronous callback to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) | Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses an asynchronous callback to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) | Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses a promise to return the result. |
| [getFormsInfo](arkts-form-formhost-getformsinfo-f-sys.md#getFormsInfo-(System-API)) | Obtains the widget information provided by a specified application on the device (excluding template widgets). This API uses a promise to return the result. |
| [getTemplateFormsInfo](arkts-form-formhost-gettemplateformsinfo-f-sys.md#getTemplateFormsInfo) | Obtains the template widget information provided by a specified application on the device. This API uses a promise to return the result. |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#isSystemReady) | Checks whether the system is ready. This API uses an asynchronous callback to return the result. |
| [isSystemReady](arkts-form-formhost-issystemready-f-sys.md#isSystemReady-(System-API)) | Checks whether the system is ready. This API uses a promise to return the result. |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyFormsEnableUpdate) | Instructs the widgets to enable or disable updates. This API uses an asynchronous callback to return the result. |
| [notifyFormsEnableUpdate](arkts-form-formhost-notifyformsenableupdate-f-sys.md#notifyFormsEnableUpdate-(System-API)) | Instructs the widgets to enable or disable updates. This API uses a promise to return the result. |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyFormsPrivacyProtected) | Notifies that the privacy protection status of the specified widgets changes. This API uses an asynchronous callback to return the result. |
| [notifyFormsPrivacyProtected](arkts-form-formhost-notifyformsprivacyprotected-f-sys.md#notifyFormsPrivacyProtected-(System-API)) | Notifies that the privacy protection status of the specified widgets changes. This API uses a promise to return the result. |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyFormsVisible) | Instructs the widgets to make themselves visible. This API uses an asynchronous callback to return the result. |
| [notifyFormsVisible](arkts-form-formhost-notifyformsvisible-f-sys.md#notifyFormsVisible-(System-API)) | Instructs the widgets to make themselves visible. This API uses a promise to return the result. |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyInvisibleForms) | Instructs the widget framework to make a widget invisible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses an asynchronous callback to return the result. |
| [notifyInvisibleForms](arkts-form-formhost-notifyinvisibleforms-f-sys.md#notifyInvisibleForms-(System-API)) | Instructs the widget framework to make a widget invisible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses a promise to return the result. |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyVisibleForms) | Instructs the widget framework to make a widget visible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses an asynchronous callback to return the result. |
| [notifyVisibleForms](arkts-form-formhost-notifyvisibleforms-f-sys.md#notifyVisibleForms-(System-API)) | Instructs the widget framework to make a widget visible. After this API is called, **onVisibilityChange** is invoked to notify the widget provider. This API uses a promise to return the result. |
| [offChangeSceneAnimationState](arkts-form-formhost-offchangesceneanimationstate-f-sys.md#offChangeSceneAnimationState) | Cancels listening to the event of change scene animation state. You can use this method to cancel listening to the event of change scene animation state. |
| [offDeleteFormsCallback](arkts-form-formhost-offdeleteformscallback-f-sys.md#offDeleteFormsCallback) | Unregister the callback for deleting forms. |
| [offFormOverflow](arkts-form-formhost-offformoverflow-f-sys.md#offFormOverflow) | Cancels listening to the event of formOverflow. You can use this method to cancel listening to the event of formOverflow. |
| [offFormUninstall](arkts-form-formhost-offformuninstall-f-sys.md#offFormUninstall) | Cancels listening to the event of uninstall form. You can use this method to cancel listening to the event of uninstall form. |
| [offGetFormRect](arkts-form-formhost-offgetformrect-f-sys.md#offGetFormRect) | Cancels listening to the event of get form rect. You can use this method to cancel listening to the event of get form rect. |
| [offGetLiveFormStatus](arkts-form-formhost-offgetliveformstatus-f-sys.md#offGetLiveFormStatus) | Cancels Listening to the event of get live form status. |
| [offGetWantParamsCallback](arkts-form-formhost-offgetwantparamscallback-f-sys.md#offGetWantParamsCallback) | Unregister callback of getting the want parameters of the form. |
| [offTemplateFormDetailInfoChange](arkts-form-formhost-offtemplateformdetailinfochange-f-sys.md#offTemplateFormDetailInfoChange) | Unsubscribes from changes in the static configuration information of template widgets. This API uses an asynchronous callback to return the result. |
| [offUpdateFormsConfigCallback](arkts-form-formhost-offupdateformsconfigcallback-f-sys.md#offUpdateFormsConfigCallback) | Unregister the callback for updating form config. |
| off_changeSceneAnimationState | Unsubscribes from the event of switching the interactive widget state. An interactive widget can be in the active or inactive state. In the inactive state, the interactive widget is the same as a common widget. In the active state, the interactive widget can start the **LiveFormExtensionAbility** process developed by the widget host to implement interactive widget animations. This API uses an asynchronous callback to return the result. |
| off_formOverflow | Unsubscribes from the interactive widget animation request event. This API uses an asynchronous callback to return the result. |
| off_formUninstall | Unsubscribes from widget uninstall events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget > is automatically uninstalled. |
| off_getFormRect | Unsubscribes from the event of requesting widget position and dimension. This API uses an asynchronous callback to return the result. |
| off_getLiveFormStatus | Cancels Listening to the event of get live form status. |
| [onChangeSceneAnimationState](arkts-form-formhost-onchangesceneanimationstate-f-sys.md#onChangeSceneAnimationState) | Listens to the event of change scene animation state. You can use this method to listen to the event of change scene animation state. |
| [onDeleteFormsCallback](arkts-form-formhost-ondeleteformscallback-f-sys.md#onDeleteFormsCallback) | Register the callback for deleting forms. |
| [onFormOverflow](arkts-form-formhost-onformoverflow-f-sys.md#onFormOverflow) | Listens to the event of formOverflow. You can use this method to listen to the event of formOverflow. |
| [onFormUninstall](arkts-form-formhost-onformuninstall-f-sys.md#onFormUninstall) | Listens to the event of uninstall form. You can use this method to listen to the event of uninstall form. |
| [onGetFormRect](arkts-form-formhost-ongetformrect-f-sys.md#onGetFormRect) | Listens to the event of get form rect. You can use this method to listen to the event of get form rect. |
| [onGetLiveFormStatus](arkts-form-formhost-ongetliveformstatus-f-sys.md#onGetLiveFormStatus) | Listens to the event of get live form status. |
| [onGetWantParamsCallback](arkts-form-formhost-ongetwantparamscallback-f-sys.md#onGetWantParamsCallback) | Register callback of getting the want parameters of the form. |
| [onTemplateFormDetailInfoChange](arkts-form-formhost-ontemplateformdetailinfochange-f-sys.md#onTemplateFormDetailInfoChange) | Subscribes to changes in the static configuration information of template widgets. This API uses an asynchronous callback to return the result. |
| [onUpdateFormsConfigCallback](arkts-form-formhost-onupdateformsconfigcallback-f-sys.md#onUpdateFormsConfigCallback) | Register the callback for updating form config. |
| on_changeSceneAnimationState | Subscribes to the event of switching the interactive widget state. An interactive widget can be in the active or inactive state. In the inactive state, the interactive widget is the same as a common widget. In the active state, the interactive widget can start the **LiveFormExtensionAbility** process developed by the widget host to implement interactive widget animations. This API uses an asynchronous callback to return the result. |
| on_formOverflow | Subscribes to the interactive widget animation request event. This API uses an asynchronous callback to return the result. |
| on_formUninstall | Subscribes to widget uninstall events. This API uses an asynchronous callback to return the result. > **NOTE：**> > Widget uninstall is different from widget removal. When an application is uninstalled, the corresponding widget > is automatically uninstalled. |
| on_getFormRect | Subscribes to the event of requesting widget position and dimension. This API uses an asynchronous callback to return the result. |
| on_getLiveFormStatus | Listens to the event of get live form status. |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverForms) | Recovers recycled widgets and updates their status to non-recyclable, or updates the status of widgets to non- recyclable if the widgets are not recycled. This API uses a promise to return the result. |
| [recoverForms](arkts-form-formhost-recoverforms-f-sys.md#recoverForms-(System-API)) | Recovers widgets. This API uses an asynchronous callback to return the result. |
| [recycleForms](arkts-form-formhost-recycleforms-f-sys.md#recycleForms) | Recycles widgets, that is, reclaiming widget memory. This API uses a promise to return the result. |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseForm) | Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager still retains the widget cache and storage information. This API uses an asynchronous callback to return the result. |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseForm-(System-API)) | Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager retains the storage information about the widget and retains or releases the cache information based on the setting. This API uses an asynchronous callback to return the result. |
| [releaseForm](arkts-form-formhost-releaseform-f-sys.md#releaseForm-(System-API)) | Releases a widget. After this API is called, the application can no longer use the widget, but the Widget Manager retains the storage information about the widget and retains or releases the cache information based on the setting. This API uses a promise to return the result. |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestForm) | Requests a widget update. This API uses an asynchronous callback to return the result. |
| [requestForm](arkts-form-formhost-requestform-f-sys.md#requestForm-(System-API)) | Requests a widget update. This API uses a promise to return the result. |
| [requestFormWithParams](arkts-form-formhost-requestformwithparams-f-sys.md#requestFormWithParams) | Carries parameters to request a widget update. This API uses a promise to return the result. |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setFormsRecyclable) | Sets widgets to be recyclable. This API uses a promise to return the result. |
| [setFormsRecyclable](arkts-form-formhost-setformsrecyclable-f-sys.md#setFormsRecyclable-(System-API)) | Sets widgets to be recyclable. This API uses an asynchronous callback to return the result. |
| [setPublishFormResult](arkts-form-formhost-setpublishformresult-f-sys.md#setPublishFormResult) | Sets the result for the operation of adding a widget to the home screen. |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setRouterProxy) | Sets a router proxy for widgets and obtains the Want information required for redirection. This API uses an asynchronous callback to return the result. > **NOTE：**> > Generally, for a widget added to the home screen, in the case of router-based redirection, the widget framework > checks whether the destination is proper and whether the widget has the redirection permission, and then > triggers redirection accordingly. For a widget that is added to a widget host and has a router proxy configured, > in the case of router-based redirection, the widget framework does not trigger redirection for the widget. > - Only one router proxy can be set for a widget. If multiple proxies are set, only the last proxy takes effect. |
| [setRouterProxy](arkts-form-formhost-setrouterproxy-f-sys.md#setRouterProxy-(System-API)) | Sets a router proxy for widgets and obtains the Want information required for redirection. This API uses a promise to return the result. This API uses a promise to return the result. > **NOTE：**> > - Generally, for a widget added to the home screen, in the case of router-based redirection, the widget framework > checks whether the destination is proper and whether the widget has the redirection permission, and then > triggers redirection accordingly. For a widget that is added to a widget host and has a router proxy configured, > in the case of router-based redirection, the widget framework does not trigger redirection for the widget. > > - Only one router proxy can be set for a widget. If multiple proxies are set, only the last proxy takes effect. |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareForm) | Shares a specified widget with a remote device. This API uses an asynchronous callback to return the result. |
| [shareForm](arkts-form-formhost-shareform-f-sys.md#shareForm-(System-API)) | Shares a specified widget with a remote device. This API uses a promise to return the result. |
| [updateFormLocation](arkts-form-formhost-updateformlocation-f-sys.md#updateFormLocation) | Updates the widget location. |
| [updateFormLockedState](arkts-form-formhost-updateformlockedstate-f-sys.md#updateFormLockedState) | Notifies the update of the widget lock state. This API uses a promise to return the result. If an application is locked, its widget will also be locked and masked in a locked style. To use the widget, you need to enter the password set for the widget. |
| [updateFormSize](arkts-form-formhost-updateformsize-f-sys.md#updateFormSize) | Updates the size of the widget. |
<!--DelEnd-->


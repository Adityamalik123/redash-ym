import React from "react";
import PropTypes from "prop-types";
import cx from "classnames";
import { clientConfig, currentUser } from "@/services/auth";
import Tooltip from "antd/lib/tooltip";
import Alert from "antd/lib/alert";

export default function EmailSettingsWarning({ featureName, className, mode, adminOnly }) {
  if (!clientConfig.mailSettingsMissing) {
    return null;
  }

  if (adminOnly && !currentUser.isAdmin) {
    return null;
  }

  const message = (
    <span>
      Your mail server isn&apos;t configured correctly, and is needed for {featureName} to work.{" "}
    </span>
  );

  if (mode === "icon") {
    return (
      <Tooltip title={message}>
        <i className={cx("fa fa-exclamation-triangle", className)} />
      </Tooltip>
    );
  }

  return <Alert message={message} type="error" className={className} />;
}

EmailSettingsWarning.propTypes = {
  featureName: PropTypes.string.isRequired,
  className: PropTypes.string,
  mode: PropTypes.oneOf(["alert", "icon"]),
  adminOnly: PropTypes.bool,
};

EmailSettingsWarning.defaultProps = {
  className: null,
  mode: "alert",
  adminOnly: false,
};

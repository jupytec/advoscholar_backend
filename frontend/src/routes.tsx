import { lazy, Suspense } from "react";
import { type RouteObject } from "react-router-dom";

const Index = lazy(() => import("@/pages/index"));
const Notfound = lazy(() => import("@/pages/404"));
const Login = lazy(() => import("@/pages/auth/login"))
const VerifyEmail = lazy(() => import("@/pages/auth/verify"))
const ForgotPasssword = lazy(() => import("@/pages/auth/forgotten"))
const Signup = lazy(() => import("@/pages/auth/signup"))
const SetPassword = lazy(() => import("@/pages/auth/setPassword"))

export const routes: Array<RouteObject> = [
  {
    index: true,
    element: (
      <Suspense>
        <Index />
      </Suspense>
    ),
  },
  {
    path: "/login",
    element: (
      <Suspense>
        <Login />
      </Suspense>
    ),
  },
  {
    path: "/verify_email",
    element: (
      <Suspense>
        <VerifyEmail />
      </Suspense>
    ),
  },
  {
    path: "/forgot_password",
    element: (
      <Suspense>
        <ForgotPasssword />
      </Suspense>
    ),
  },
  {
    path: "/signup",
    element: (
      <Suspense>
        <Signup />
      </Suspense>
    ),
  },
  {
    path: "set_password",
    element: (
      <Suspense>
        <SetPassword />
      </Suspense>
    ),
  },
  {
    path: "*",
    element: (
      <Suspense>
        <Notfound />
      </Suspense>
    ),
  },
  
];

export default routes;
